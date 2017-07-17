<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1>Music Packs Search</h1>
            </div>
        </div>
        <div class="space-60"></div>
        <div class="row">
            <div class="col-md-12">
                <ul class="product-filter-block list-inline clearfix">
                    <li> Title </li>
                    <li class="active"><a href="#">Top rated</a></li>
                    <li><a href="#">Otra categoría</a></li>
                    <li><a href="#"> Una última</a></li>
                </ul>
                <a href="#" @click.prevent="get_products()"> Clickeme </a>
                <a href="#" @click.prevent="items=[]"> Borrar </a>
                <music-pack-list :items="items"></music-pack-list>

            </div>
        </div>
        <div class="space-60"></div>
    </div>
</template>

<script>
    import MusicpackList from './MusicPackList.vue'

    export default {
        data () {
            return {
                items: [ ]
            }
        },
        methods:{
            get_products() {
                let vm = this;
                let url = vm.url_backend + '/site/music-packs';

                $.ajax({
                    url: url,
                    data:{ id: vm.id },
                    success: function (result) {
                        vm.items = result;
                    }
                });
            },
        },
        components: {
            musicPackList: MusicpackList,
        }
    }
</script>