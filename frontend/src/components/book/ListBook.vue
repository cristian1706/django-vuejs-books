<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                
                <div>
                    <h2>Book list</h2>
                    <b-button size="sm" :to="{name: 'NewBook'}" variant="primary">New book</b-button>
                </div>
                <br>
                
                <div class="col-md-12">
                    <b-table striped hover :items="books" :fields="fields">
                        
                        <template v-slot:cell(action)="row">
                            <b-button size="sm" variant="primary" :to="{ name:'EditBook', params:{bookId: row.item.id} }">
                                Edit
                            </b-button>
                            <b-button size="sm" variant="danger" :to="{ name:'DeleteBook', params:{bookId: row.item.id} }">
                                Delete
                            </b-button>
                        </template>

                    </b-table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            fields: [
                { key: 'title', label: 'Title' },
                { key: 'description', label: 'Description' },
                { key: 'action', label: 'Action' }
            ],
            books: []
        }
    },
    methods: {
        
        getBooks() {
            const path = 'http://localhost:8000/books/'
            axios.get(path).then((response) => {
                this.books = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getBooks()
    }
}
</script>

<style lang="css" scoped>
</style>