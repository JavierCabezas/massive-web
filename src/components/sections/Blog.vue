<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1>Blog</h1>
            </div>
        </div>

        <div class="space-60"></div>
        <div class="container" id="blog-post-list">
            <div v-for="(post, index) in posts">
                <div class="blog-item col-sm-4" v-if="is_index_in_range(index)">
                    <a href="#">
                        <img :src="post.image" class="img-responsive" :alt="post.name">
                    </a>
                    <div class="blog-desc">
                        <ul v-if="post.tags.length > 0">
                            <li v-for="tag in post.tags">
                            <a href="#" class="tag">
                                <i class="fa fa-tag"></i> {{tag.name}} </a> &nbsp;
                            </li>
                        </ul>
                        <p v-else> <br> </p>
                        <h4 class="title">
                            <a :href="'#/blog/'+post.id"> #{{post.id}} {{post.name}} </a>
                        </h4>
                        <p>  {{post.intro}} </p>
                        <a :href="'#/blog/'+post.id" class="btn btn-skin">Continue</a>
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

    export default {
        name: 'blog-post-list',
        data () {
            return {
                posts: [ ],
                items_per_page: 3,
                current_page: 1
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
            paginate: Paginate
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