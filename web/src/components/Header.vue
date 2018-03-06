<template>
    <section class="hero is-primary is-bold">
        <div class="hero-body">
            <div class="container has-text-centered">
                <h1 class="title">
                    &#x1F649; Emoji Index &#x1F64A;
                </h1>
                <h2 class="subtitle">
                    search &amp; filter emoji
                </h2>
                <div>
                    <ul class="buttons has-addons is-centered" id="nav-ul">
                        <li class="button is-rounded">
                            <router-link to="/" exact @click.native="updateStyle($event)">home</router-link>
                        </li>

                        <li class="button is-rounded">
                            <router-link to="/about" exact @click.native="updateStyle($event)">about</router-link>
                        </li>

                        <li class="button is-rounded">
                            <router-link to="/api" exact @click.native="updateStyle($event)">api</router-link>
                        </li>

                        <li class="button is-rounded">
                            <router-link to="/contact" exact @click.native="updateStyle($event)">contact</router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
</template>


<script>
    import About from './About.vue';

    export default {
        props: {
            title: {
                type: String,
                required: true
            }
        },

        components: {
            'app-about': About
        },

        data() {
            return {
                show_about: false
            }
        },

        methods: {
            updateStyle: function(event) {
                // Get all li elements from ul.
                let children = document.getElementById('nav-ul').children;

                // Remove 'clicked' class each li.
                for(let i = 0; i < children.length; i++) {
                    let child = children[i];
                    child.classList.remove('clicked');
                }

                // Add 'clicked' class to the selected li.
                event.target.parentElement.classList.add('clicked');   
            },

            styleInitialActive: function() {
                // Add 'clicked' class to initial selected li.
                let active_link = document.getElementsByClassName('router-link-active')[0];

                active_link.parentElement.classList.add('clicked');
            }
        },

        mounted() {
            this.styleInitialActive();
        }
    }
</script>


<style scoped>
a {
    color: #ab9bdc;
}

li .router-link-active {
    font-weight: bold;
    color: white;
}

.clicked {
    background: #3f1b8c;
}
</style>