<template>
    <div class="row">
        <div class="col-sm-4" v-for="item in items">
            <div class="item_holder">
                <a :href="'#/music-pack/'+item.id"><img :src="item.img" alt="" class="img-responsive"></a>
                <div class="title">
                    <h5>{{item.title}}</h5>
                    <span class="price">{{item.price}}</span>
                    <p>{{item.text}}</p>
                </div>
            </div>
        </div>
        <paginate
                :pageCount="10"
                :containerClass="'pagination'"
                :clickHandler="clickCallback">
        </paginate>
    </div>
</template>

<script>
    import Paginate from 'vuejs-paginate'

    export default {
        props: ['items'],
        components: {
            paginate: Paginate
        },
        methods: {
            clickCallback: function(page) {
                console.log(page)
            }
        }
    }
</script>