<template>
    <div>
        <section>
            <div class="container top-space">
                <div class="tile is-ancestor is-mobile">
                    <div class="tile is-parent is-6 has-text-centered">

                        <div class="tile is-child notification is-warning">
                            <div class="columns">
                                <div class="column emoji_display ld ld-jump" style="animation-direction:normal; animation-duration:3.0s">
                                    <a v-on:click="copy" ref="clickedemoji">
                                        {{ click_emoji.surrogate_pairs }}
                                    </a>
                                </div>
                                <div class="column title">
                                    <p class="title">Click Me</p>
                                    <p class="arrow left">{{ left_arrow }}</p>
                                    <p class="subtitle">to copy me to clipboard</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="tile is-parent is-6 has-text-centered">
                        <div class="tile is-child notification is-danger">
                            <div class="columns">
                                <div class="column title">
                                    <p class="title">Hover Over</p>
                                    <p class="arrow right">{{ right_arrow }}</p>
                                    <p class="subtitle">me to view my shortcode</p>
                                </div>
                                <b-tooltip v-bind:label="hover_emoji.shortcode">
                                    <div class="column emoji_display ld ld-jump" style="animation-direction:reverse; animation-duration:3.5s">
                                        <a>
                                            {{ hover_emoji.surrogate_pairs }}
                                        </a>
                                    </div>
                                </b-tooltip>
                            </div>
                        </div>

                    </div>
                
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <p class="title is-4 has-text-centered" style="color: #4c421a;">
                    Emoji Index makes it fun to search, filter, and explore
                    the latest emoji
                </p>
            </div>
        </section>

        <section class="hero is-success">
            <div class="hero-body">
                <div class="container">
                    <nav class="level">
                    <div class="level-item has-text-centered">
                        <div>
                            <p class="heading">Total Emoji</p>
                            <p class="title">
                                {{ stats['Total Emojis'] | locale-string }}
                            </p>
                        </div>
                    </div>
                    <div class="level-item has-text-centered">
                        <div>
                            <p class="heading">Recent Emoji</p>
                            <p class="title">
                                {{ stats['Recently Added Emojis'] | locale-string }}
                            </p>
                        </div>
                    </div>
                    <div class="level-item has-text-centered">
                        <div>
                            <p class="heading">Keywords</p>
                            <p class="title">
                                {{ stats['Total Keywords'] | locale-string }}
                            </p>
                        </div>
                    </div>
                    <div class="level-item has-text-centered">
                        <div>
                            <p class="heading">Categories</p>
                            <p class="title">
                                {{ stats['Total Sub Categories'] | locale-string }}
                            </p>
                        </div>
                    </div>
                </nav>
                </div>
            </div>
        </section>
    </div>
    
</template>


<script>
    export default {
        data() {
            return {
                click_emoji: {
                    surrogate_pairs: '\ud83c\udf6a',
                    shortcode: ':cookie:'
                },
                hover_emoji: {
                    surrogate_pairs: '\ud83d\udc7b',
                    shortcode: ':ghost:'
                },
                left_arrow: '\u2b05\ufe0e',
                right_arrow: '\u27a1\ufe0e',
                }
        },

        methods: {
            copy() {
                this.$clipboard(this.$refs.clickedemoji.innerText);
                this.$toast.open('Copied!')
            }
        },

        computed: {
            message() {
                return this.$store.state.message;
            },

            stats() {
                return this.$store.state.stats;
            }
        },

        created() {
            console.log('ABOUT COMPONENT CREATED');
            this.$store.dispatch('fetchMessage');
            this.$store.dispatch('fetchStats');
        }
    }
</script>


<style scoped>
a {
    text-decoration: none !important;
}

.top-space {
    margin-top: 50px;
}

.bottom-space {
    margin-bottom: 50px;
}

@keyframes bounceleft {
    0%, 20%, 60%, 100% {
        -webkit-transform: translateY(0);
        transform: translateY(0);
    }

    40% {
        -webkit-transform: translateX(-20px);
        transform: translateX(-20px);
    }

    80% {
        -webkit-transform: translateX(-10px);
        transform: translateX(-10px);
    }
}

@keyframes bounceright {
    0%, 20%, 60%, 100% {
        -webkit-transform: translateY(0);
        transform: translateY(0);
    }

    40% {
        -webkit-transform: translateX(20px);
        transform: translateX(20px);
    }

    80% {
        -webkit-transform: translateX(10px);
        transform: translateX(10px);
    }
}

.emoji_display {
    font-size: 7em;
}

.arrow{
    font-size: 50px;
}

.arrow.left {
    animation: bounceleft 1s infinite;
}

.arrow.right {
    animation: bounceright 1s infinite;
}

.hero.is-success {
    /*background-color: #f1f1f1;*/
    background-color: #efe9ff;
    color: #504a4a;
}

.hero.is-success .title {
    color: #504a4a;
}

.notification.is-danger {
    /*background-color: #9056bb;*/
    background-color: #272229;
}

/*.notification.is-warning {
    background-color: #642194;
    color: white;
}*/
</style>