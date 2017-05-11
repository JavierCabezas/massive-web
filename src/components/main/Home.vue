<template>
    <div>
        <slider> </slider>
        <div class="space-60"></div>

        <features> </features>
        <div class='space-60'></div>

        <products-slider :products="featured_products"></products-slider>
        <div class="space-50"></div>

        <blog-entries> </blog-entries>
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
                 featured_products: [
                     { id: 1,  img: "../../src/img/women/1.jpg",  link: '#' },
                     { id: 2,  img: "../../src/img/women/2.jpg",  link: '#' },
                     { id: 3,  img: "../../src/img/women/3.jpg",  link: '#' },
                     { id: 4,  img: "../../src/img/women/4.jpg",  link: '#' },
                     { id: 5,  img: "../../src/img/women/5.jpg",  link: '#' },
                     { id: 6,  img: "../../src/img/women/6.jpg",  link: '#' },
                     { id: 7,  img: "../../src/img/women/7.jpg",  link: '#' },
                     { id: 8,  img: "../../src/img/men/1.jpg",  link: '#' },
                     { id: 9,  img: "../../src/img/men/2.jpg",  link: '#' },
                     { id: 10,  img: "../../src/img/men/3.jpg",  link: '#' },
                     { id: 11,  img: "../../src/img/men/4.jpg",  link: '#' },
                     { id: 12,  img: "../../src/img/men/5.jpg",  link: '#' }
                 ]
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