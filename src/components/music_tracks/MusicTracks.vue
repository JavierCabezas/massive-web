<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1> {{ t('music_tracks') }}</h1>
            </div>
        </div>
        <bread-crumbs :crumbs="crumbs"></bread-crumbs>
        <div class="space-60"></div>
        <div class="row">
            <div class="col-md-8">
                <music-track-list :items="items"></music-track-list>
            </div>
            <music-categories :categories="categories"
                              :selected_category_index="selected_category_index"
                              @category_changed="get_music_tracks"
            ></music-categories>
        </div>
    </div>
</template>

<script>
    import MusicTrackList from './MusicTrackList.vue'
    import BreadCrumbs from '../main/Breadcrumbs.vue'
    import MusicCategories from './../music_packs/MusicPacksCategories.vue'

    export default {
        locales: {
            es_ES: {
                music_tracks: 'Canciones sueltas',
            },
            en_US: {
                music_tracks: 'Music Tracks',
            }
        },
        data () {
            return {
                items: [ ],
                packs: {},
                categories: {},
                selected_category_index: -1,
                crumbs: {
                    nav: [
                        {
                            link: 'home',
                            name_en: 'Home',
                            name_es: 'Inicio'
                        }
                    ],
                    current: {
                        es: 'Canciones sueltas',
                        en: 'Music tracks'
                    }
                }
            }
        },
        created: function () {
            this.get_categories();
            this.get_music_tracks();
            this.get_music_packs();
        },
        methods: {
            get_music_tracks: function(category_index = -1) {
                let vm = this;
                let url = vm.url_backend + 'music_track/index';
                let category_id = -1;
                if(category_index > -1){
                    category_id = vm.categories[category_index].id;
                    vm.selected_category_index = category_index;
                }else{
                    vm.selected_category_index = -1;
                }

                $.ajax({
                    url: url,
                    data: { category_id: category_id },
                    success: function (result) {
                        vm.items = result;
                    }
                });
            },
            get_music_packs: function(){
                let vm = this;
                let url = vm.url_backend + 'music_track/index';
                $.ajax({
                    url: url,
                    success: function (result) {
                        vm.packs = result;
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
            MusicTrackList,
            MusicCategories,
            BreadCrumbs
        }
    }
</script>