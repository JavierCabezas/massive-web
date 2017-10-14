<template>
    <section class="featured-products" id="featured-products">
        <div class="container">
            <h2 class="section-heading"> {{ title }} </h2>
            <div class="row">
                <ul class="popularslider">
                    <li class="slide item_holder" v-for="p in products">
                        <router-link  tag="a" :to="{ name: 'music-pack-detail', params: { id: p.id} }" >
                            <h4 class="title" v-if="$translate.current == 'en_US'"> {{p.title}} </h4>
                            <h4 class="title" v-if="$translate.current == 'es_ES'"> {{p.title_es}} </h4>
                            <img :src="p.img">
                        </router-link>
                    </li>
                </ul>
            </div>
        </div>
    </section>
</template>

<script>
    export default {
        name: 'featured-products',
        props: ['products', 'title'],
        data () {
            return {
                slider: null
            }
        },
        watch: {
            products: function (val) {
              this.start_slider();
            },
            '$route.params.id'(newId) {
                this.$emit('changed_user', newId);
                $('html, body').animate({ scrollTop: 0 }, 'slow');
            }
        },
        methods:{
            start_slider() {
                if(this.slider !== null){
                    this.slider.destroySlider();
                }

                this.$nextTick(function() {
                    this.slider = $(".popularslider").bxSlider({
                        slideWidth: 200,
                        minSlides: 1,
                        maxSlides: 6,
                        slideMargin: 10,
                        auto: true
                    });
                });
            }
        }
    }
</script>