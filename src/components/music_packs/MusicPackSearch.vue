<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1>Music Packs Search</h1>
            </div>
        </div>
        <div class="space-60"></div>
        <div class="row">
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
                    <a href="#" @click.prevent="get_products()"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                    <a href="#" @click.prevent="get_products()"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                    <a href="#" @click.prevent="get_products()"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                    <a href="#" @click.prevent="get_products()"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                    <a href="#" @click.prevent="get_products()"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                    <a href="#" @click.prevent="get_products()"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                    <a href="#" @click.prevent="get_products()"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                    <a href="#" @click.prevent="get_products()"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                    <a href="#" @click.prevent="get_products()"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                    <a href="#" @click.prevent="get_products()"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                    <a href="#" @click.prevent="get_products()"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                    <a href="#" @click.prevent="get_products()"><div class="col-sm-12 col-md-2 option">Music Type</div></a>
                </section>
            </div>

            <div class="col-sm-12 col-md-offset-1 col-md-10">
                <a href="#" @click.prevent="get_products()"> Clickeme </a>
                <a href="#" @click.prevent="items=[]"> Borrar </a>
                <music-pack-list :items="items"></music-pack-list>

            </div>
        </div>
        <div class="space-60"></div>
    </div>
</template>

<script>
    import MusicpackList from './MusicPackList.vue'

    export default {
        data () {
            return {
                items: [ ],
                content_to_show: " "
            }
        },
        methods:{
            get_products() {
                let vm = this;
                let url = vm.url_backend + '/site/music-packs';

                $.ajax({
                    url: url,
                    data:{ id: vm.id },
                    success: function (result) {
                        vm.items = result;
                    }
                });
            },
            show_content: function(type_of_content) {
                this.content_to_show = type_of_content
            },
        },
        components: {
            musicPackList: MusicpackList,
        }
    }
</script>