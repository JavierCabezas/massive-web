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
                <h4 v-if="selected_category_index == -1"> {{ t('view_all') }}</h4>
                <h4 v-if="selected_category_index > 0">
                    {{t('view_one') }}
                    <span v-if="$translate.current == 'en_US'"> {{ categories[selected_category_index].name_en }}</span>
                    <span v-if="$translate.current == 'es_ES'"> {{ categories[selected_category_index].name_es }}</span>
                </h4>

                <music-pack-list :items="items" v-if="items.length > 0"></music-pack-list>
                <p v-if="items.length === 0"> {{ t('no_elements') }} </p>
            </div>

            <div class="col-md-3 col-md-offset-1">
                <div class="sidebar-widget">
                    <h3> {{ t('filter') }}</h3>
                    <ul class="list-unstyled">
                        <li><a href="#" @click.prevent="load_music_packs()"> {{ t('all_categories') }} </a></li>
                        <li v-for="(c, idx) in categories">
                            <a v-if="$translate.current == 'en_US'" href="#" @click.prevent="load_music_packs(idx)"> {{c.name_en}} </a>
                            <a v-if="$translate.current == 'es_ES'" href="#" @click.prevent="load_music_packs(idx)"> {{c.name_es}} </a>
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
                all_categories: 'Todas',
                view_all: 'Viendo todas las categorías',
                view_one: 'Viendo elementos de ',
                no_elements: 'No hay elementos disponibles para estos filtros'
            },
            en_US: {
                music_packs: 'Music packs',
                filter: 'Filter by category',
                all_categories: 'All',
                view_all: 'Showing all categories',
                view_one: 'Showing elements from ',
                no_elements: 'There are no avaiable elements for this filter'
            }
        },
        data () {
            return {
                items: [],
                categories: [],
                selected_category_index: -1
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
                }
                $.ajax({
                    url: vm.url_backend + 'music_pack/index',
                    data: { category_id: category_id },
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