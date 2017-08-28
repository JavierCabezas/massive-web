<template>
    <div>
        <div class="space-60"></div>
        <div class="container">
            <div  class="row single-product">
                <div class="col-md-9">
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
                                <h3 class="title"><a href="#"> {{product.title}} </a></h3>
                                <h4>Autor</h4>
                                <span class="price"> {{product.price}}</span>
                                <span class="rating">
                                <a href="#">2 reviews</a>
                            </span>
                                <div class="add-buttons">
                                    <a href="#" data-toggle="tooltip" data-placement="top" title="Add to cart"
                                       class="btn btn-skin btn-lg"><i class="fa fa-shopping-cart"></i> {{ t('add_cart') }}</a>
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
                                    <span v-html="product.description">  </span>
                                    <div class="space-40"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>

                <div class="col-md-3" v-if="product.categories.length > 0">
                    <div class="sidebar-widget">
                        <h3>Categories</h3>
                        <ul class="list-unstyled">
                            <li v-for="category in product.categories">
                                <a href="#"> {{ category }}</a>
                            </li>
                        </ul>
                    </div><!--sidebar-widget end-->
                </div><!--sidebar col-->
            </div>
            <div class="space-60"></div>
            <div class="similar-products">
                <div class="row">
                    <product-slider :products="featured_products"></product-slider>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import ProductSlider from '../main/ProductsSlider.vue'
    import Playlist from './Playlist.vue'

    export default {
        name: 'featured-products',
        data () {
            return {
                id: this.$route.params.id,
                product: { id: null, img: null, title: null, price: null, author: null, description: null, tracks: [], categories: []  },
                featured_products: [
                    { id: 1,  img: "../../src/img/women/1.jpg",  link: '#' },  { id: 2,  img: "../../src/img/women/2.jpg",  link: '#' },  { id: 3,  img: "../../src/img/women/3.jpg",  link: '#' },
                    { id: 4,  img: "../../src/img/women/4.jpg",  link: '#' },  { id: 5,  img: "../../src/img/women/5.jpg",  link: '#' },  { id: 6,  img: "../../src/img/women/6.jpg",  link: '#' },
                    { id: 7,  img: "../../src/img/women/7.jpg",  link: '#' },  { id: 8,  img: "../../src/img/men/1.jpg",  link: '#' },  { id: 9,  img: "../../src/img/men/2.jpg",  link: '#' }, { id: 10,  img: "../../src/img/men/3.jpg",  link: '#' }, { id: 11,  img: "../../src/img/men/4.jpg",  link: '#' },
                ]
            }
        },
        mounted () {
            this.start_slider()
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
            productSlider: ProductSlider,
            playlist: Playlist
        },
        created: function () {
            let vm = this;
            let url = vm.url_backend + 'music_pack/' + vm.id;

            $.ajax({
                url: url,
                success: function (result) {
                    vm.product = result;
                }
            });
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