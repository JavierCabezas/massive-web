<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1>{{post.title}}</h1>
            </div>
        </div>
        <div class="row">
            <div class="blog-item col-sm-10 col-sm-offset-1">
                <div class="blog-desc">
                    <img :src="post.img" class="img-responsive" alt="">
                    <p v-html="post.summary"> </p>
                    <div class="categories">
                        <a href="" class="tag"><i class="fa fa-tag"></i> </a>
                        <ul>
                            <li v-for="cat in post.tags">
                                {{cat}}
                            </li>
                        </ul>
                    </div>

                </div>

                <a href="/#/blog"> Back to posts </a>
            </div>
        </div>
    </div>
</template>

<script>
    export default{
        data() {
            return {
                id: this.$route.params.id,
                watch: {
                    '$route'(to, from){
                        this.id = params.id;
                    }
                },
                post: []
            }
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