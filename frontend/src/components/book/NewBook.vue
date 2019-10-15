<template lang="html">
    <div class="container">
        
        <div class="row">
            <div class="col text-left">
                <h2>New book</h2>
            </div>
        </div>
        
        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        
                        <form @submit="onSubmit">
                        
                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Title</label>
                                <div class="col-sm-6">
                                    <input type="text" placeholder="Enter title..." name="title" class="form-control" v-model.trim="form.title">
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="description" class="col-sm-2 col-form-label">Description</label>
                                <div class="col-sm-6">
                                    <textarea name="description" class="form-control" placeholder="Enter description..." rows="3" v-model.trim="form.description"></textarea>
                                </div>
                            </div>

                            <div class="rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="primary">Create</b-button>
                                    <b-button type="submit" class="btn-large-space" :to="{ name: 'ListBook' }">Cancel</b-button>
                                </div>
                            </div>
                        
                        </form>
                    
                    </div>
                </div>
            </div>
        </div>
    
    </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'

export default {
    data() {
        return {
            form: {
                title: '',
                description: ''
            },
        }
    },
    methods: {
        onSubmit(evt) {
            evt.preventDefault()

            const path = 'http://localhost:8000/books/'

            axios.post(path, this.form).then((response) => {
                this.form.title = response.data.title
                this.form.description = response.data.description
                swal("Book created succesfully!", "", "success")
            })
            .catch((error) => {
                console.log(error)
                swal("The book could not be created", "", "error")
            })
        },
    },

    created() {
        
    }
}
</script>

<style lang="css" scoped>
</style>