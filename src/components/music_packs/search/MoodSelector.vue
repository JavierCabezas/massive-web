<template>
    <div class="row">
        <section class="col-sm-offset-1 col-sm-10 option-search">
            <h3>Choose an Option!</h3>
            <a href="#" @click.prevent="show_content('music_type')" v-for="item in mood">
                <div class="col-sm-12 col-md-6 option">{{item.type}}</div>
            </a>
        </section>

        <transition name="fade">
            <section v-if="content_to_show == 'music_type'" class="col-sm-offset-1 col-sm-10 musictype-search">
                <h3>Choose a Music Style!</h3>
                <a href="#" @click.prevent="get_parent_products(1)" v-for="item in genre">
                    <div class="col-sm-12 col-md-2 option">{{item.type}}</div>
                </a>
            </section>
        </transition>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                content_to_show: " ",
                mood: [
                    {
                        type: 'Positivo'
                    },
                    {
                        type: 'Negativo'
                    },
                    {
                        type: 'Activo'
                    },
                    {
                        type: 'Pasivo'
                    }
                ],
                genre: [
                    {
                        type: 'Genre 1'
                    },
                    {
                        type: 'Genre 2'
                    },
                    {
                        type: 'Genre 3'
                    },
                    {
                        type: 'Genre 4'
                    },
                    {
                        type: 'Genre 5'
                    },
                    {
                        type: 'Genre 6'
                    },
                    {
                        type: 'Genre 7'
                    },
                    {
                        type: 'Genre 8'
                    },
                    {
                        type: 'Genre 9'
                    },
                    {
                        type: 'Genre 10'
                    },
                    {
                        type: 'Genre 11'
                    },
                    {
                        type: 'Genre 12'
                    },
                ]
            }
        },
        methods:{
            show_content: function(type_of_content) {
                this.content_to_show = type_of_content
            },
            get_parent_products: function(data){
                this.$emit('get_parent_products', data)
            }
        }
    }
</script>

<style>
    .fade-enter-active, .fade-leave-active {
    transition: opacity 1s
    }
    .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0
    }
</style>