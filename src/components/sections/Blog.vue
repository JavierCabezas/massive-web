<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1>Blog</h1>
            </div>
        </div>

        <div class="space-60"></div>
        <div class="container" id="blog-post-list">
            <div v-for="post in posts" class="col-sm-4">
                <div class="blog-item">
                    <a href="#">
                        <img :src="post.img" class="img-responsive" alt="">
                    </a>
                    <div class="blog-desc">
                        <ul v-if="post.tags.length > 0">
                            <li v-for="tag in post.tags">
                            <a href="#" class="tag">
                                <i class="fa fa-tag"></i> {{tag}} </a> &nbsp;
                            </li>
                        </ul>
                        <p v-else> <br> </p>
                        <h4 class="title">
                            <a :href="'#/blog/'+post.id"> {{post.title}} </a>
                        </h4>
                        <p>  {{post.text}} </p>
                        <a :href="'#/blog/'+post.id" class="btn btn-skin">Continue</a>
                    </div><!--blog desc-->
                </div><!--blog item-->
            </div><!--grid blog-->
            <nav>
                <ul class="pagination pull-right clearfix">
                    <li>
                        <a href="#" aria-label="Previous">
                            <span aria-hidden="true">«</span>
                        </a>
                    </li>
                    <li class="active"><a href="#">1</a></li>
                    <li><a href="#">2</a></li>
                    <li><a href="#">3</a></li>
                    <li><a href="#">4</a></li>
                    <li><a href="#">5</a></li>
                    <li>
                        <a href="#" aria-label="Next">
                            <span aria-hidden="true">»</span>
                        </a>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'blog-post-list',
        data () {
            return {
                posts: [
                    {
                        id: 1,
                        img: '../src/img/bg/bg-1.jpg',
                        title: 'Title 2',
                        text: 'INGLÉS Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum commodo tellus nisl, ac fermentum ligula laoreet eu. In consequat diam sed est tempus convallis.',
                        tags: ['tag1', 'tag2', 'tag3']
                    },
                    {
                        id: 2,
                        img: '../src/img/bg/bg-1.jpg',
                        title: 'Título 3',
                        text: 'INGLÉS Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum commodo tellus nisl, ac fermentum ligula laoreet eu. In consequat diam sed est tempus convallis.',
                        tags: []
                    },
                    {
                        id: 3,
                        img: '../src/img/bg/bg-1.jpg',
                        title: 'Title 4',
                        text: 'INGLÉS Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum commodo tellus nisl, ac fermentum ligula laoreet eu. In consequat diam sed est tempus convallis.',
                        tags: ['tag7', 'tag8', 'tag9']
                    }
                ]
            }
        }
    }
</script>