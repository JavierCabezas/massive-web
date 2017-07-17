<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1>Music Packs Search</h1>
            </div>
        </div>
        <div class="space-60"></div>
        <div class="row">
            <section class="col-sm-offset-1 col-sm-10">
                <div class="col-sm-12 col-md-6">Positivo</div>
                <div class="col-sm-12 col-md-6">Negativo</div>
                <div class="col-sm-12 col-md-6">Activo</div>
                <div class="col-sm-12 col-md-6">Pasivo</div>
            </section>
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
                items: [ ]
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
        },
        components: {
            musicPackList: MusicpackList,
        }
    }
</script>