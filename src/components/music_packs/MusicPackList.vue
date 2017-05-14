<template>
    <div class="row">

        <div class="col-sm-4" v-for="(item, index) in items">
            <div class="item_holder" v-if="is_index_in_range(index)">
                <a :href="'#/music-pack/'+item.id"><img :src="item.img" :alt="item.title" class="img-responsive"></a>
                <div class="title">
                    <h5>{{index}} : {{item.title}}</h5>
                    <span class="price">{{item.price}}</span>
                    <p>{{item.text}}</p>
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
                return  ( this.items != null ) ?  this.items : [];
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