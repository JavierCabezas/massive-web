<template>
    <div id="cwrap">
        <div id="nowPlay">
            <h3 id="npAction">{{ t('playlist') }}</h3>
            <div id="npTitle"></div>
        </div>
        <div id="audiowrap">
            <div id="audio0">
                <audio v-if="tracks[active_track_index]" controls="controls" width="300" :src="tracks[active_track_index].file">
                    {{ t('html5_audio_support') }}
                </audio>
            </div>
            <div id="extraControls">
                <button id="btnPrev" class="ctrlbtn">|&lt;&lt; {{ t('prev_track') }}</button>
                <button id="btnNext" class="ctrlbtn"> {{ t('next_track') }} &gt;&gt;|</button>
            </div>
        </div>
        <div id="plwrap">
            <ul id="plUL">
                <li v-for="(track, index) in tracks">
                    <div class="plItem">

                            <div class="plTitle"><a href="#"> {{ track.name }}</a></div>
                            <div class="plLength">{{ track.lenght }}</div>

                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    import ProductSlider from '../main/ProductsSlider.vue'

    export default {
        name: 'featured-products',
        props: [ 'tracks' ],
        data () {
            return {
                id: this.$route.params.id,
                active_track_index: 0,
                product: null,
                featured_products: [
                    { id: 1,  img: "../../src/img/women/1.jpg",  link: '#' },  { id: 2,  img: "../../src/img/women/2.jpg",  link: '#' },  { id: 3,  img: "../../src/img/women/3.jpg",  link: '#' },
                    { id: 4,  img: "../../src/img/women/4.jpg",  link: '#' },  { id: 5,  img: "../../src/img/women/5.jpg",  link: '#' },  { id: 6,  img: "../../src/img/women/6.jpg",  link: '#' },
                    { id: 7,  img: "../../src/img/women/7.jpg",  link: '#' },  { id: 8,  img: "../../src/img/men/1.jpg",  link: '#' },  { id: 9,  img: "../../src/img/men/2.jpg",  link: '#' }, { id: 10,  img: "../../src/img/men/3.jpg",  link: '#' }, { id: 11,  img: "../../src/img/men/4.jpg",  link: '#' },
                ]
            }
        },
        locales: {
            es_ES: {
                playlist: 'Listado de canciones',
                prev_track: 'Anterior',
                next_track: 'Siguiente',
                html5_audio_support: 'Tu explorador no soporta el tag de audio HTML.'
            },
            en_US: {
                playlist: 'Playlist',
                prev_track: 'Prev. Track',
                next_track: 'Next Track',
                html5_audio_support: 'Your browser does not support the HTML5 Audio Tag.'
            }
        }
    }
</script>