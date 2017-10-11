<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1>{{post.name}}</h1>
            </div>
        </div>
        <bread-crumbs :crumbs="crumbs"></bread-crumbs>

        <div class="row">
            <div class="blog-item blog-content col-sm-10 col-sm-offset-1">
                <div class="blog-desc">
                    <img :src="post.image" class="img-responsive featured-blog" alt="">
                    <p class="whitespace"> {{post.post}} </p>
                    <div class="categories">
                        <p>Tags</p>
                        <ul>
                            <li v-for="tag in post.tags">
                                <i class="fa fa-tag"></i>  {{tag.name}}
                            </li>
                        </ul>
                    </div>

                </div>

                <router-link tag="a" :to="{name:'blog'}"> {{ t('back') }} </router-link>
            </div>
        </div>
    </div>
</template>

<script>
    import BreadCrumbs from '../main/Breadcrumbs.vue'

    export default{
         locales: {
            es_ES: {
                back: 'Volver a los posts',
            },
            en_US: {
                back: 'Back to posts',
            }
        },
        data() {
            return {
                id: this.$route.params.id,
                watch: {
                    '$route'(to, from){
                        this.id = params.id;
                    }
                },
                crumbs: {
                    nav: [
                        {
                            link: 'home',
                            name_en: 'Home',
                            name_es: 'Inicio'
                        },
                        {
                            link: 'blog',
                            name_en: 'Blog',
                            name_es: 'Blog'
                        }
                    ],
                    current: {
                        es: 'Post',
                        en: 'Post'
                    }
                },
                post: []
            }
        },
        components: {
            BreadCrumbs
        },
        created: function () {
            let vm = this;
            let id = this.$route.params.id;
            let url = vm.url_backend + 'blog/post/' + id;
            $.ajax({
                url: url,
                success: function (result) {
                    vm.post = result;
                }
            });
        },
    }
</script>

<style>
    .whitespace {
        white-space: pre-wrap;
    }
</style>