<template>
    <section>
        <p>Post ID: {{id}} </p>
        <div class="space-60"></div>
        <div class="container">
            <div class="row">
                <div class="blog-item col-sm-10 col-sm-offset-1">
                    <a href="#">
                        <img src="" class="img-responsive" alt="">
                    </a>
                    <div class="blog-desc">
                        <a href="" class="tag"><i class="fa fa-tag"></i> </a>
                        <h4 class="title"><a href="#"> {{post.title}} </a></h4>
                        <p> {{post.summary}}</p>
                        <p class="lead">{{post.info}}</p>

                    </div><!--blog desc-->
                    <div class="comments">
                        <h3><i class="pe-7s-comment"></i></h3>
                        <div class="media">
                            <div class="media-left">
                                <img class="media-object img-circle" width="60" src="../../img/team-1.jpg" alt="...">
                            </div>
                            <div class="media-body">
                                <h4 class="media-heading">John Doe <a href="#">Reply</a></h4>
                                <p>
                                    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book
                                </p>
                            </div>
                        </div>
                    </div>

                    <a href="/#/blog"> Back to posts </a>
                </div>
            </div>
        </div>
        <div class="space-60"></div>
    </section>
</template>

<script>
    export default{
        data() {
            return {
                id: this.$route.params.id,
                watch: {
                    '$route'(to, from){
                        this.id = params.id;
                        //To-do: Do an ajax call to update the blog post
                    }
                },
                post: {
                        id: 1,
                        title: "I mean, they have no respect for us up there! No respect whatsoever!",
                        summary: "We're all just drudgeons to them! Unbelievable! Some idiot disabled his firewall, meaning all the computers on Seven are teeming with ... ",
                        info: "Plus I've just had to walk all the way down the motherfudging stairs, because the lifts are broken AGAIN! It's my term for my time of the month. Oh. What time of the month? The weekend? So, remember the new number! 0118 999! 88199, 9119 725! ... 3! Hello, IT. Have you tried turning it off and on again? A gay musical, called Gay. That's quite gay. Gay musical? Aren't all musicals gay? This must be, like, the gayest musical ever. <br> Oh my God. I didn't even know Smarties made a cereal. They don't. It's just Smarties in a bowl with milk. You're not comfortable with your sexuality? Oh, I'm very comfortable with my sexuality, I just don't want to be slapped in the face with their sexuality. So, remember the new number! 0118 999! 88199, 9119 725! ... 3! I mean, they have no respect for us up there! No respect whatsoever! We're all just drudgeons to them! Today I have a business empire the like of which the world has never seen the like of which. I hope it doesn't sound arrogant when I say that I am the greatest man in the world! No, no, that's the music you heard when it come on.",
                        comments: '1 comment',
                        tags: [ 'tag1', 'tag5']
                }
            }
        }
    }
</script>