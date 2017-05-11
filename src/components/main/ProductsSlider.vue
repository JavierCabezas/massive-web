<template>
    <section class="featured-products" id="featured-products">
        <div class="container">
            <h2 class="section-heading"> Popular Items</h2>
            <div class="row">
                <ul class="popularslider">
                    <li class="slide item_holder" v-for="p in products">
                        <img :src="p.img">
                    </li>
                </ul>
            </div>
        </div>
    </section>
</template>

<script>
    export default {
        name: 'featured-products',
        props: ['products'],
        data () {
            return {

            }
        },
        mounted () {
            this.start_slider()
        },
        methods:{
            start_slider(){
                    $(".popularslider").bxSlider({
                        slideWidth: 200,
                        minSlides: 3,
                        maxSlides: 6,
                        slideMargin: 10,
                        auto: true
                    });
            }
        }
    }
</script>