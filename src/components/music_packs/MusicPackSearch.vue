<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1>Music Packs Search</h1>
            </div>
        </div>
        <div class="space-60"></div>
        <div class="row">
           <mood-selector v-on:get_parent_products="get_products"></mood-selector>
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
    import MoodSelector from './search/MoodSelector.vue'

    export default {
        data () {
            return {
                items: [ ],
            }
        },
        methods:{
            get_products() {
                let vm = this;
                let url = vm.url_backend + '/music-pack/index';

                $.ajax({
                    url: url,
                    data:{ id: vm.id },
                    success: function (result) {
                        vm.items = result;
                    }
                });
            }
        },
        components: {
            musicPackList: MusicpackList,
            moodSelector: MoodSelector
        }
    }
</script>