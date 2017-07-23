<template>
    <div>
        <section class="col-sm-offset-1 col-sm-10 option-search">
            <h3>Choose an Option!</h3>
            <a href="#" @click.prevent="show_content('music_type')"><div class="col-sm-12 col-md-6 option">Positivo</div></a>
            <a href="#" @click.prevent="show_content('music_type')"><div class="col-sm-12 col-md-6 option">Negativo</div></a>
            <a href="#" @click.prevent="show_content('music_type')"><div class="col-sm-12 col-md-6 option">Activo</div></a>
            <a href="#" @click.prevent="show_content('music_type')"><div class="col-sm-12 col-md-6 option">Pasivo</div></a>
        </section>

        <div v-if="content_to_show == 'music_type'">
            <section class="col-sm-offset-1 col-sm-10 musictype-search">
                <h3>Choose a Music Style!</h3>
                <a href="#" @click.prevent="get_parent_products(1)"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                <a href="#" @click.prevent="get_parent_products(2)"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                <a href="#" @click.prevent="get_parent_products(3)"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                <a href="#" @click.prevent="get_parent_products(4)"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                <a href="#" @click.prevent="get_parent_products(5)"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                <a href="#" @click.prevent="get_parent_products(6)"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                <a href="#" @click.prevent="get_parent_products(7)"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                <a href="#" @click.prevent="get_parent_products(8)"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                <a href="#" @click.prevent="get_parent_products(9)"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                <a href="#" @click.prevent="get_parent_products(10)"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                <a href="#" @click.prevent="get_parent_products(11)"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                <a href="#" @click.prevent="get_parent_products(12)"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
            </section>
        </div>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                content_to_show: " "
            }
        },
        methods:{
            show_content: function(type_of_content) {
                this.content_to_show = type_of_content
            },
            get_parent_products: function(data){
                this.$emit('get_parent_products', data)
            }
        }
    }
</script>