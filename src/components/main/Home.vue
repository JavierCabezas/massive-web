<template>
    <div>
        <slider> </slider>
        <div class="space-60"></div>

        <features> </features>
        <div class='space-60'></div>

        <products-slider :products="featured_products"></products-slider>
        <div class="space-50"></div>

        <blog-entries :blog_posts="last_blog_posts"> </blog-entries>
        <div class="space-50"></div>

        <partners> </partners>

        <newsletter> </newsletter>
     </div>
 </template>

 <script>
     import Slider from './Slider.vue'
     import Features from './Features.vue'
     import ProductsSlider from './ProductsSlider.vue'
     import BlogEntires from './BlogEntires.vue'
     import Partners from './Partners.vue'
     import Newsletter from './Newsletter.vue'

     export default {
         data () {
             return {
                 featured_products: {},
                 last_blog_posts: {}
             }
         },
         created: function () {
            this.get_blog_posts();
         },
         methods:{
            get_blog_posts() {
                let vm = this;
                let url = vm.url_backend + 'blog/posts';
                let limit = 4;
                $.ajax({
                    url: url + '/' + limit,
                    success: function (result) {
                        vm.last_blog_posts = result;
                    }
                });
            }
         },
         components: {
             slider: Slider,
             features: Features,
             productsSlider: ProductsSlider,
             blogEntries: BlogEntires,
             partners: Partners,
             newsletter: Newsletter
         }
     }
 </script>