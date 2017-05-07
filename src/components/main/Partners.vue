<template>
    <section class="partners container" id="partners">
        <h2 class="section-heading">Partners</h2>
        <ul class="partnerslider">
            <li><img src="../../img/partner.png"/></li>
            <li><img src="../../img/partner.png"/></li>
            <li><img src="../../img/partner.png"/></li>
            <li><img src="../../img/partner.png"/></li>
            <li><img src="../../img/partner.png"/></li>
            <li><img src="../../img/partner.png"/></li>
            <li><img src="../../img/partner.png"/></li>
            <li><img src="../../img/partner.png"/></li>
            <li><img src="../../img/partner.png"/></li>
        </ul>
    </section>
</template>

<script>
    export default {
        name: 'partners',
        data () {
            return {

            }
        },
        mounted () {
            this.start_slider()
        },
        methods:{
            start_slider(){
                $(".partnerslider").bxSlider({
                    slideWidth: 200,
                    minSlides: 3,
                    maxSlides: 6,
                    slideMargin: 10,
                    auto: true
                });
            }
        }
    }
</script>