<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1>Music Packs</h1>
            </div>
        </div>
        <bread-crumbs></bread-crumbs>
        <div class="space-60"></div>
        <div class="row">
            <div class="col-md-8">
                <ul class="product-filter-block list-inline clearfix">
                    <li> Title </li>
                    <li class="active"><a href="#">Top rated</a></li>
                    <li><a href="#">Otra categoría</a></li>
                    <li><a href="#"> Una última</a></li>
                </ul>

                <music-pack-list :items="items"></music-pack-list>

            </div>

            <div class="col-md-3 col-md-offset-1">
                <div class="sidebar-widget">
                    <h3>Categories</h3>
                    <ul class="list-unstyled">
                        <li><a href="#">New Arrivals</a></li>
                        <li><a href="#">Men</a></li>
                        <li><a href="#">Women</a></li>
                        <li><a href="#">T-shirts</a></li>
                        <li><a href="#">Shoes</a></li>
                        <li><a href="#">Handbags</a></li>
                        <li><a href="#">Accessories</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="space-60"></div>
    </div>
</template>

<script>
    import MusicpackList from './MusicPackList.vue'
    import BreadCrumbs from '../main/Breadcrumbs.vue'

    export default {
        data () {
            return {
                items: [ ]
            }
        },
        created: function () {
            let vm = this;
            let url = vm.url_backend + 'music_pack/index';

            $.ajax({
                url: url,
                success: function (result) {
                    vm.items = result;
                }
            });
        },
        components: {
            musicPackList: MusicpackList,
            breadCrumbs: BreadCrumbs
        }
    }
</script>