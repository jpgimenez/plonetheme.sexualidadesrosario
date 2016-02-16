module.exports = function (grunt) {
    'use strict';
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        // we could just concatenate everything, really
        // but we like to have it the complex way.
        // also, in this way we do not have to worry
        // about putting files in the correct order
        // (the dependency tree is walked by r.js)
        less: {
            dist: {
                options: {
                    paths: [],
                    strictMath: false,
                    sourceMap: true,
                    outputSourceFiles: true,
                    sourceMapURL: '++theme++plonetheme.sexualidadesrosario/styles.css.map',
                    sourceMapFilename: 'src/plonetheme/sexualidadesrosario/theme/styles.css.map',
                    modifyVars: {
                        "isPlone": "false"
                    }
                },
                files: {
                    'src/plonetheme/sexualidadesrosario/theme/styles.css': 'src/plonetheme/sexualidadesrosario/theme/styles.less'
                }
            }
        },

        watch: {
            scripts: {
                files: ['src/plonetheme/sexualidadesrosario/theme/styles.less',
                        'src/plonetheme/sexualidadesrosario/theme/startbootstrap-sexualidadesrosario/less/*.less'],
                tasks: ['less']
            }
        },
        browserSync: {
            html: {
                bsFiles: {
                    src : ['src/plonetheme/sexualidadesrosario/theme/styles.less',
                           'src/plonetheme/sexualidadesrosario/theme/startbootstrap-sexualidadesrosario/less/*.less']
                },
                options: {
                    watchTask: true,
                    debugInfo: true,
                    server: {
                        baseDir: "."
                    }
                }
            },
            plone: {
                bsFiles: {
                    src : ['src/plonetheme/sexualidadesrosario/theme/styles.less',
                           'src/plonetheme/sexualidadesrosario/theme/startbootstrap-sexualidadesrosario/less/*.less']
                },
                options: {
                    watchTask: true,
                    debugInfo: true,
                    proxy: "localhost:8080"
                }
            }
        }
    });

    // grunt.loadTasks('tasks');
    grunt.loadNpmTasks('grunt-browser-sync');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.registerTask('default', ['watch']);
    grunt.registerTask('bsync', ["browserSync:html", "watch"]);
    grunt.registerTask('plone-bsync', ["browserSync:plone", "watch"]);
};
