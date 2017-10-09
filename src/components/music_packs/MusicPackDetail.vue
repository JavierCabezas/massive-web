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

                                <div class="add-buttons">
                                    <a @click.prevent="add_item_to_cart()" href="#" data-toggle="tooltip" data-placement="top" title="Add to cart"  class="btn btn-skin btn-lg">
                                        <i class="fa fa-shopping-cart"></i> {{ t('add_cart') }}
                                    </a>
                                </div>
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
                    <product-slider :products="product.similar" @changed_user="load_product"></product-slider>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import ProductSlider from '../main/ProductsSlider.vue'
    import Playlist from './Playlist.vue'
    import BreadCrumbs from '../main/Breadcrumbs.vue'
    import { store } from '../../main'

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
                }
            }
        },
        locales: {
            es_ES: {
                description: 'Descripción',
                add_cart: 'Añadir al carro',
                author: 'Autor',
                category: 'Categoría'
            },
            en_US: {
                description: 'Description',
                add_cart: 'Add to cart',
                author: 'Author',
                category: 'Category'
            }
        },
        filters: {
            cash: function (value) {
              const pieces = parseFloat(value).toFixed(2).split('');
              let ii = pieces.length - 3;
              while ((ii-=3) > 0) {
                pieces.splice(ii, 0, ',')
              }
              return "$" + pieces.join('')
            },
            nl2br: function (value){
                return (value + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1' + '<br>' + '$2');
            }
        },
        components: {
            productSlider: ProductSlider,
            playlist: Playlist,
            breadCrumbs: BreadCrumbs
        },
        created: function () {
            this.load_product(this.id);
        },
        methods:{
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
                    }
                });
            },
            add_item_to_cart(){
                let vm = this;
                let swal_texts = { 'swal_title':'', 'text': '', 'confirm_button_text': '', 'cancel_button_text': '' };
                store.commit('add_music_pack_to_cart', {music_pack: vm.product, quantity: 1});
                if(this.$translate.current === 'en_US'){
                    swal_texts.title = 'Success';
                    swal_texts.text = 'You added ' + vm.title + ' to your shopping cart. Do you want to continue shopping?';
                    swal_texts.confirm_button_text = 'Yes, I will add more items';
                    swal_texts.cancel_button_text = 'No, take me to checkout';
                }
                else{
                    swal_texts.title = 'Éxito';
                    swal_texts.text = 'Agregaste ' + vm.title_es + ' a tu carro de compras. ¿Quieres continuar comprando?';
                    swal_texts.confirm_button_text = 'Sí, quiero agregar más productos';
                    swal_texts.cancel_button_text = 'No, llevarme al carro';
                }

                this.$swal({
                    title: swal_texts.title,
                    text: swal_texts.text,
                    type: 'success',
                    showCancelButton: true,
                    confirmButtonText: swal_texts.confirm_button_text,
                    cancelButtonText: swal_texts.cancel_button_text
                }).then(function() {
                    alert("cambiar de página aquí!");
                }, function(dismiss) { });
            }
        }
    }
</script>

<style>
    .whitespace {
        white-space: pre-wrap;
    }
</style>