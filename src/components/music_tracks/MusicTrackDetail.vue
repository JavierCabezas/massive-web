<template>
    <div>
        <bread-crumbs></bread-crumbs>
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
                                <player :track="product.track"></player>
                            </div>
                        </div>
                    </div><!--single product details end-->
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
        </div>
    </div>
</template>

<script>
    import ProductSlider from '../main/ProductsSlider.vue'
    import Playlist from './Player.vue'
    import BreadCrumbs from '../main/Breadcrumbs.vue'

    export default {
        name: 'featured-products',
        data () {
            return {
                id: this.$route.params.id,
                product: { id: null, img: null, title: null, price: null, author: null, description: null, tracks: [], categories: []  }
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
            playlist: Playlist,
            breadCrumbs: BreadCrumbs
        },
        created: function () {
            let vm = this;
            let url = vm.url_backend + '/site/music-track';

            $.ajax({
                url: url,
                data:{ id: vm.id },
                success: function (result) {
                    vm.product = result;
                }
            });
        }
    }
</script>