<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1> {{t('music_packs')}}</h1>
            </div>
        </div>
        <bread-crumbs :crumbs="crumbs"></bread-crumbs>
        <div class="space-60"></div>
        <div class="row">
            <div class="col-md-8">
                <h4 v-if="selected_category_index == -1"> {{ t('view_all') }}</h4>
                <h4 v-if="selected_category_index > 0">
                    {{t('view_one') }}
                    <span v-if="$translate.current == 'en_US'"> {{ categories[selected_category_index].name_en }}</span>
                    <span v-if="$translate.current == 'es_ES'"> {{ categories[selected_category_index].name_es }}</span>
                </h4>

                <music-pack-list :items="items" v-if="items.length > 0"></music-pack-list>
                <p v-if="items.length === 0"> {{ t('no_elements') }} </p>

            </div>

            <music-categories :categories="categories"
                              :selected_category_index="selected_category_index"
                              @category_changed="load_music_packs"
            ></music-categories>

        </div>
        <div class="space-60"></div>
    </div>
</template>

<script>
    import MusicpackList from './MusicPackList.vue'
    import BreadCrumbs from '../main/Breadcrumbs.vue'
    import MusicCategories from './MusicPacksCategories.vue'

    export default {
        locales: {
            es_ES: {
                music_packs: 'Packs de música',
                view_all: 'Viendo todas las categorías',
                view_one: 'Viendo elementos de ',
                no_elements: 'No hay elementos disponibles para estos filtros'
            },
            en_US: {
                music_packs: 'Music packs',
                view_all: 'Showing all categories',
                view_one: 'Showing elements from ',
                no_elements: 'There are no avaiable elements for this filter'
            }
        },
        data () {
            return {
                items: [],
                categories: [],
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
                        es: 'Packs de música',
                        en: 'Music Packs'
                    }
                }
            }
        },
        created: function () {
            this.load_music_packs();
            this.get_categories();
        },
        methods: {
            load_music_packs: function(category_index = -1) {
                let vm = this;
                let category_id = -1;

                if(category_index > -1){
                    category_id = vm.categories[category_index].id;
                    vm.selected_category_index = category_index;
                }else{
                    vm.selected_category_index = -1;
                }

                this.$http.get(
                    vm.url_backend + 'music_pack/index', {
                        params: {
                            category_id: category_id
                        }
                    })
                    .then(function(result) {
                       vm.items = result.body;
                    });
            },
            get_categories: function(){
                let vm = this;
                this.$http.get(vm.url_backend + 'categories/parents').then(function(result) {
                       vm.categories = result.body;
                });
            }
        },
        components: {
            musicPackList: MusicpackList,
            breadCrumbs: BreadCrumbs,
            musicCategories: MusicCategories
        }
    }
</script>