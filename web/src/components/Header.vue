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
    export default {
        props: {
            title: {
                type: String,
                required: true
            }
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
.hero.is-primary.is-bold {
    background-color: #7957d5;
    background-image: url("data:image/svg+xml,%3Csvg width='180' height='180' viewBox='0 0 180 180' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M81.28 88H68.413l19.298 19.298L81.28 88zm2.107 0h13.226L90 107.838 83.387 88zm15.334 0h12.866l-19.298 19.298L98.72 88zm-32.927-2.207L73.586 78h32.827l.5.5 7.294 7.293L115.414 87l-24.707 24.707-.707.707L64.586 87l1.207-1.207zm2.62.207L74 80.414 79.586 86H68.414zm16 0L90 80.414 95.586 86H84.414zm16 0L106 80.414 111.586 86h-11.172zm-8-6h11.173L98 85.586 92.414 80zM82 85.586L87.586 80H76.414L82 85.586zM17.414 0L.707 16.707 0 17.414V0h17.414zM4.28 0L0 12.838V0h4.28zm10.306 0L2.288 12.298 6.388 0h8.198zM180 17.414L162.586 0H180v17.414zM165.414 0l12.298 12.298L173.612 0h-8.198zM180 12.838L175.72 0H180v12.838zM0 163h16.413l.5.5 7.294 7.293L25.414 172l-8 8H0v-17zm0 10h6.613l-2.334 7H0v-7zm14.586 7l7-7H8.72l-2.333 7h8.2zM0 165.414L5.586 171H0v-5.586zM10.414 171L16 165.414 21.586 171H10.414zm-8-6h11.172L8 170.586 2.414 165zM180 163h-16.413l-7.794 7.793-1.207 1.207 8 8H180v-17zm-14.586 17l-7-7h12.865l2.333 7h-8.2zM180 173h-6.613l2.334 7H180v-7zm-21.586-2l5.586-5.586 5.586 5.586h-11.172zM180 165.414L174.414 171H180v-5.586zm-8 5.172l5.586-5.586h-11.172l5.586 5.586zM152.933 25.653l1.414 1.414-33.94 33.942-1.416-1.416 33.943-33.94zm1.414 127.28l-1.414 1.414-33.942-33.94 1.416-1.416 33.94 33.943zm-127.28 1.414l-1.414-1.414 33.94-33.942 1.416 1.416-33.943 33.94zm-1.414-127.28l1.414-1.414 33.942 33.94-1.416 1.416-33.94-33.943zM0 85c2.21 0 4 1.79 4 4s-1.79 4-4 4v-8zm180 0c-2.21 0-4 1.79-4 4s1.79 4 4 4v-8zM94 0c0 2.21-1.79 4-4 4s-4-1.79-4-4h8zm0 180c0-2.21-1.79-4-4-4s-4 1.79-4 4h8z' fill='%23f4f2f6' fill-opacity='0.13' fill-rule='evenodd'/%3E%3C/svg%3E");
}

a {
    color: #8970d8;
}

li .router-link-active {
    font-weight: bold;
    color: white;
}

.clicked {
    background: #3f1b8c;
}
</style>