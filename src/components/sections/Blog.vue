<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1>Blog</h1>
            </div>
        </div>
        <bread-crumbs :crumbs="crumbs"></bread-crumbs>

        <div class="space-60"></div>
        <div class="container" id="blog-post-list">
            <div v-for="(post, index) in posts">
                <div class="blog-item col-sm-4" v-if="is_index_in_range(index)">
                    <router-link  tag="a" :to="{ name: 'blog-post', params: { id: post.id} }" >
                        <img :src="post.image" class="img-responsive" :alt="post.name">
                    </router-link>
                    <div class="blog-desc">
                        <ul v-if="post.tags.length > 0">
                            <li v-for="tag in post.tags">
                            <a v-if="false" href="#" class="tag">
                                <i class="fa fa-tag"></i> {{tag.name}} </a> &nbsp;
                            </li>
                        </ul>
                        <p v-else> <br> </p>
                        <h4 class="title">
                            <router-link  tag="a" :to="{ name: 'blog-post', params: { id: post.id} }" >{{post.name}} </router-link>
                        </h4>
                        <p>  {{post.intro}} </p>
                    </div>
                </div>
            </div>

            <paginate
                    :pageCount="posts.length / items_per_page"
                    :containerClass="'pagination'"
                    :clickHandler="clickCallback">
            </paginate>

        </div>
    </div>
</template>

<script>
    import Paginate from 'vuejs-paginate'
    import BreadCrumbs from '../main/Breadcrumbs.vue'

    export default {
        name: 'blog-post-list',
        data () {
            return {
                posts: [ ],
                items_per_page: 3,
                current_page: 1,
                crumbs: {
                    nav: [
                        {
                            link: 'home',
                            name_en: 'Home',
                            name_es: 'Inicio'
                        }
                    ],
                    current: {
                        es: 'Blog',
                        en: 'Blog'
                    }
                }
            }
        },
        created: function () {
            let vm = this;
            let url = vm.url_backend + 'blog/posts';

            $.ajax({
                url: url,
                success: function (result) {
                    vm.posts = result;
                }
            });
        },
        components: {
            Paginate,
            BreadCrumbs
        },
        methods: {
            clickCallback: function(page) {
                this.current_page = page;
            },
            is_index_in_range(index){
                let item_number = index +1;
                return item_number > ( (this.current_page -1 ) * this.items_per_page ) && item_number <= ( (this.current_page ) * this.items_per_page)
            }
        }
    }
</script>