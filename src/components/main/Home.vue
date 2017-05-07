<template>
    <div>
        <slider> </slider>
        <div class="space-60"></div>

        <features> </features>
        <div class='space-60'></div>

        <products-slider></products-slider>
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