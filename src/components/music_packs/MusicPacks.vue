<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1> {{t('music_packs')}}</h1>
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
                    <h3> {{ t('filter') }}</h3>
                    <ul class="list-unstyled">
                        <li><a href="#"> {{ t('all_categories') }} </a></li>
                        <li v-for="c in categories">
                            <a v-if="$translate.current == 'en_US'" href="#"> {{c.name_en}} </a>
                            <a v-if="$translate.current == 'es_ES'" href="#"> {{c.name_es}} </a>
                        </li>
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
        locales: {
            es_ES: {
                music_packs: 'Packs de música',
                filter: 'Filtro por categoría',
                all_categories: 'Todas'
            },
            en_US: {
                music_packs: 'Music packs',
                filter: 'Filter by category',
                all_categories: 'All'
            }
        },
        data () {
            return {
                items: [],
                categories: []
            }
        },
        created: function () {
            this.load_music_packs();
            this.get_categories();
        },
        methods: {
            load_music_packs: function() {
                let vm = this;
                $.ajax({
                    url: vm.url_backend + 'music_pack/index',
                    success: function (result) {
                        vm.items = result;
                    }
                });
            },
            get_categories: function(){
                let vm = this;
                $.ajax({
                    url: vm.url_backend + 'categories/parents',
                    success: function (result) {
                        vm.categories = result;
                    }
                });
            }
        },
        components: {
            musicPackList: MusicpackList,
            breadCrumbs: BreadCrumbs
        }
    }
</script>