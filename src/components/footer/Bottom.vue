<template>
    <footer class="footer-bottom">
        <div class="container text-center">
            <div class="logo col-sm-12 col-md-offset-4 col-md-4">
                <router-link tag="a" :to="{name: 'home'}">
                    <img src="../../img/mw-logo2.png" alt="">
                </router-link>
            </div>
            <img src="../../img/payment.png" alt="" class="img-responsive payment">
            <span class="copyright col-sm-12 col-md-offset-3 col-md-6">Copyright 2016 &copy; MassiveWave</span>
            <ul class="redes-footer clearfix list-inline text-center">
                <li>
                    <a href="http://www.facebook.com/MassiveWaveVGM" class="social-icon si-dark si-dark-round si-facebook">
                        <i class="fa fa-facebook"></i>
                    </a>
                </li>
                <li>
                    <a href="http://www.twitter.com/MassiveWaveVGM" class="social-icon si-dark si-dark-round si-twitter">
                        <i class="fa fa-twitter"></i>
                    </a>
                </li>
                <li>
                    <a href="https://www.youtube.com/channel/UCIUWbgbiw2suR_4OJrO6GtA" class="social-icon si-dark si-dark-round si-youtube">
                        <i class="fa fa-youtube"></i>
                    </a>
                </li>
            </ul>
        </div>
    </footer>
</template>