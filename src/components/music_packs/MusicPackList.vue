<template>
    <div class="row">
        <div class="col-sm-4" v-for="(item, index) in items" v-if="is_index_in_range(index)">
            <div class="item_holder">
                <router-link  tag="a" :to="{ name: 'music-pack-detail', params: { id: item.id} }" >
                    <img :src="item.img" :alt="item.title" class="img-responsive">
                </router-link>

                <div class="title">
                    <h5 v-if="$translate.current == 'en_US'"> #{{item.id}} : {{item.title}}</h5>
                    <h5 v-if="$translate.current == 'es_ES'"> #{{item.id}} : {{item.title_es}}</h5>
                    <span class="price">{{item.price | cash }}</span>
                    <p v-if="$translate.current == 'en_US'">{{item.text}}</p>
                    <p v-if="$translate.current == 'es_ES'">{{item.text_es}}</p>
                </div>

                <p>
                    <a href="#" @click.prevent="console.log('hi')" class="btn btn-primary">
                        <span class="fa fa-eye">  </span> {{ t('details') }}
                    </a>
                    <shopping-cart-button
                        :music_track="item"
                        btn_size="btn_xs"
                    ></shopping-cart-button>
                </p>
            </div>
        </div>
        <paginate
                :pageCount="computedItems.length / items_per_page"
                :containerClass="'pagination'"
                :clickHandler="clickCallback">
        </paginate>
    </div>
</template>

<script>
    import Paginate from 'vuejs-paginate'
    import BreadCrumbs from '../main/Breadcrumbs.vue'
    import ShoppingCartButton from '../main/ShoppingCartButton.vue'

    export default {
        props: [ 'items' ],
        computed: {
            computedItems: function () {
                return  ( this.items != null ) ?  this.items : [];
            }
        },
        locales: {
            es_ES: {
                details: 'Ver más detalles'
            },
            en_US: {
                details: 'See details'
            }
        },
        data () {
            return {
                items_per_page: 12,
                current_page: 1
            }
        },
        components: {
            Paginate,
            BreadCrumbs,
            ShoppingCartButton
        },
        methods: {
            clickCallback: function(page) {
                this.current_page = page;
            },
            is_index_in_range(index){
                let item_number = index +1;
                return item_number > ( (this.current_page -1 ) * this.items_per_page ) && item_number <= ( (this.current_page ) * this.items_per_page)
            }
        }
    }
</script>