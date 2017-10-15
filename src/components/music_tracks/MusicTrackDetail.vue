<template>
    <div>
        <bread-crumbs :crumbs="crumbs"></bread-crumbs>
        <div class="space-60"></div>
        <div class="container">
            <div  class="row single-product">
                <div class="col-md-12">
                    <div class="row">
                        <div class="col-md-5 margin-b-30">
                            <div id="product-single" class="single-product-slider">
                                <div class="item">
                                    <a href="#" data-lightbox="roadtrip">
                                        <img :src="product.image" :alt="product.name" class="img-responsive">
                                    </a>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-7">
                            <div class="product-detail-desc">
                                <h3 class="title" v-if="$translate.current == 'es_ES'" href="#"> {{product.name_es}} </h3>
                                <h3 class="title" v-if="$translate.current == 'en_US'" href="#"> {{product.name}} </h3>

                                <h4 v-if="$translate.current == 'en_US'">Author: {{ product.author}}</h4>
                                <h4 v-if="$translate.current == 'es_ES'">Autor: {{ product.author}} </h4>

                                <p v-if="$translate.current == 'es_ES'" v-for="cat in product.category_es"> Categoría:
                                    <span v-for="cat in product.category"> {{ cat }} </span>
                                </p>

                                <p v-if="$translate.current == 'en_US'" > Category:
                                    <span v-for="cat in product.category"> {{ cat }} </span>
                                </p>
                                <p class="whitespace" v-if="$translate.current == 'en_US'">
                                    {{product.long_description }}
                                </p>
                                <p class="whitespace" v-if="$translate.current == 'es_ES'">
                                    {{product.long_description_es }}
                                </p>

                                <span class="price"> {{product.price | cash }}</span>

                                <div class="add-buttons">
                                    <a href="#" data-toggle="tooltip" data-placement="top" title="Add to cart"
                                       class="btn btn-skin btn-lg"><i class="fa fa-shopping-cart"></i> {{ t('add_cart') }}</a>
                                </div>
                                <player :track="product.preview"></player>
                            </div>
                        </div>
                    </div><!--single product details end-->
                </div>
            </div>
            <div class="space-60"></div>
        </div>
    </div>
</template>

<script>
    import Player from './Player.vue'
    import BreadCrumbs from '../main/Breadcrumbs.vue'

    export default {
        name: 'featured-products',
        data () {
            return {
                id: this.$route.params.id,
                crumbs: {
                    nav: [
                        {
                            link: 'home',
                            name_en: 'Home',
                            name_es: 'Inicio'
                        },
                        {
                            link: 'music-tracks',
                            name_en: 'Music Tracks',
                            name_es: 'Canciones sueltas'
                        }
                    ],
                    current: {
                        es: '-',
                        en: '-'
                    }
                },
                product: { id: null, img: null, title: null, price: null, author: null, description: null, tracks: [], cat: null   }
            }
        },
        locales: {
            es_ES: {
                description: 'Descripción',
                add_cart: 'Añadir al carro'
            },
            en_US: {
                description: 'Description',
                add_cart: 'Add to cart'
            }
        },
        components: {
            BreadCrumbs,
            Player
        },
        created: function () {
            let vm = this;
            let url = vm.url_backend + 'music_track/' + vm.id;
            $.ajax({
                url: url,
                success: function (result) {
                    vm.product = result;
                    vm.crumbs.current.es = result.name_es;
                    vm.crumbs.current.en = result.name
                }
            });
        }
    }
</script>

<style scoped>
    .whitespace {
        white-space: pre-wrap;
    }
</style>