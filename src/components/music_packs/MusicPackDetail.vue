<template>
    <div>
        <bread-crumbs :crumbs="crumbs"></bread-crumbs>
        <div class="space-60"></div>
        <div class="container">
            <div class="row text-center"  v-show="!has_loaded">
                <img src="../../img/loading.gif" />
            </div>
            <div  class="row single-product" v-show="has_loaded">
                <div class="col-md-12">
                    <div class="row">
                        <div class="col-md-5 margin-b-30">
                            <div id="product-single" class="single-product-slider">
                                <div class="item">
                                    <a href="#" data-lightbox="roadtrip"> <img :src="product.img" :alt="product.title" class="img-responsive"></a>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-7">
                            <div class="product-detail-desc">
                                <h3 class="title" v-if="$translate.current == 'en_US'"> {{product.title}} </h3>
                                <h3 class="title" v-if="$translate.current == 'es_ES'"> {{product.title_es}} </h3>

                                <h4> {{ t('author') }} </h4>
                                <span class="price"> Price: {{product.price | cash }}</span>
                                <span> {{ t('category') }}: {{product.category }} </span>

                                <p v-if="$translate.current == 'en_US'">{{product.short_description}}</p>
                                <p v-if="$translate.current == 'es_ES'">{{product.short_description_es}}</p>

                                <shopping-cart-button
                                        :music_track="null"
                                        :music_pack="product"
                                ></shopping-cart-button>
                                <playlist :tracks="product.tracks"></playlist>
                            </div>
                        </div>
                    </div><!--single product details end-->
                    <div class="row">
                        <div class="col-md-12 item-more-info">
                            <div id="detail">
                                <div class="col-sm-12">
                                    <h2>{{ t('description') }}</h2>
                                    <span class="whitespace"  v-if="$translate.current == 'en_US'"> {{ product.long_description }} </span>
                                    <span class="whitespace"  v-if="$translate.current == 'es_ES'"> {{ product.long_description_es }} </span>
                                    <div class="space-40"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
            <div class="space-60"></div>
            <div class="similar-products">
                <div class="row">
                    <product-slider :title="t('similar_products') ":products="product.similar" @changed_user="load_product"></product-slider>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import ProductSlider from '../main/ProductsSlider.vue'
    import Playlist from './Playlist.vue'
    import BreadCrumbs from '../main/Breadcrumbs.vue'
    import ShoppingCartButton from '../main/ShoppingCartButton.vue'

    export default {
        name: 'featured-products',
        data () {
            return {
                id: this.$route.params.id,
                product: { id: null, img: null, title: null, price: null, author: null, description: null, tracks: [], similar: [], category: ''  },
                crumbs: {
                    nav: [
                        {
                            link: 'home',
                            name_en: 'Home',
                            name_es: 'Inicio'
                        },
                        {
                            link: 'music-packs',
                            name_en: 'Music packs',
                            name_es: 'Packs de música'
                        }
                    ],
                    current: {
                        es: '-',
                        en: '-'
                    }
                },
                has_loaded: false
            }
        },
        locales: {
            es_ES: {
                description: 'Descripción',
                author: 'Autor',
                category: 'Categoría',
                similar_products: 'Productos similares'
            },
            en_US: {
                description: 'Description',
                author: 'Author',
                category: 'Category',
                similar_products: 'Similar products'
            }
        },
        filters: {
            nl2br: function (value){
                return (value + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1' + '<br>' + '$2');
            }
        },
        components: {
            ProductSlider,
            Playlist,
            BreadCrumbs,
            ShoppingCartButton
        },
        created: function () {
            this.load_product(this.id);
        },
        methods: {
            load_product(id){
                let vm = this;
                let url = vm.url_backend + 'music_pack/' + id;
                console.log(url);
                $.ajax({
                    url: url,
                    success: function (result) {
                        vm.product = result;
                        vm.crumbs.current.en = result.title;
                        vm.crumbs.current.es = result.title_es;
                        vm.has_loaded = true;
                    }
                });
            }
        }
    }
</script>

<style>
    .whitespace {
        white-space: pre-wrap;
    }
</style>