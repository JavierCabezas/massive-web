<template>
    <div class="row">
        <div class="col-sm-4" v-for="item in items">
            <div class="item_holder">
                <a :href="item.link"><img :src="item.img" alt="" class="img-responsive"></a>
                <div class="title">
                    <h5>{{item.title}}</h5>
                    <span class="price">{{item.price}}</span>
                    <p>{{item.text}}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['items']
    }
</script>