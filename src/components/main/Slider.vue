<template>
    <div class="row">
        <div id="slider">
            <div class="slides">
                <div class="slider">
                    <div class="images">
                        <img src="../../img/slider-1_en.jpg" />
                    </div>
                </div>
                <div class="slider">
                    <div class="images">
                        <img src="../../img/slider-2_en.jpg" />
                    </div>
                </div>
                <div class="slider">
                    <div class="images">
                        <img src="../../img/slider-3_en.jpg" />
                    </div>
                </div>
                <div class="slider">
                    <div class="images">
                        <img src="../../img/slider-4_en.jpg" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'slider',
        data () {
            return {

            }
        },
        mounted () {
            this.start_slider()
        },
        methods:{
            start_slider(){
                $(".slides").bxSlider({auto:true});
            }
        }
    }
</script>