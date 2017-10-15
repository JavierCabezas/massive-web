<template>
    <div class="row">

        <div class="col-sm-4" v-for="(item,index) in items" v-if="is_index_in_range(index)">
            <div class="item_holder">
                <router-link  tag="a" :to="{ name: 'music-track-detail', params: { id: item.id} }" >
                    <img :src="item.image" :alt="item.title" class="img-responsive">
                </router-link>

                <div class="title">
                    <h5 v-if="$translate.current == 'en_US'"> {{index}} : {{item.name}}</h5>
                    <h5 v-if="$translate.current == 'es_ES'"> {{index}} : {{item.name_es}}</h5>
                    <span class="price">{{item.price | cash }}</span>
                    <p v-if="$translate.current == 'es_ES'">{{item.short_description_es}}</p>
                    <p v-if="$translate.current == 'en_US'">{{item.short_description}}</p>
                </div>
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

    export default {
        props: [ 'items' ],
        computed: {
            computedItems: function () {
                return  ( this.items !== null ) ?  this.items : [];
            }
        },
        data () {
            return {
                items_per_page: 12,
                current_page: 1
            }
        },
        components: {
            paginate: Paginate
        },
        methods: {
            clickCallback: function(page) {
                this.current_page = page;
            },
            is_index_in_range(index){
                let item_number = index +1;
                return index > ( (this.current_page -1 ) * this.items_per_page ) && index <= ( (this.current_page ) * this.items_per_page)
            }
        }
    }
</script>