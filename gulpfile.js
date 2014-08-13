var gulp = require('gulp');

var coffee = require('gulp-coffee');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var imagemin = require('gulp-imagemin');
var sourcemaps = require('gulp-sourcemaps');
var jade = require('gulp-jade');
var gulpFilter = require('gulp-filter');
var del = require('del');
var mainBowerFiles = require('main-bower-files');
var sass = require('gulp-sass');
var plumber = require('gulp-plumber');

var output_dir = 'flask_seed/static'
var paths = {
  scripts: ['src/coffee/**/*.coffee', '!src/external/**/*.coffee','!src/coffee/demo/**/*.coffee'],
  scripts_dest:output_dir+'/js',
  css_dest:output_dir+'/css',
  scss:'src/scss/**/*.scss',
  font_dest:output_dir+'/fonts',
  images: 'client/img/**/*',
  jade:'src/jade/**/*.jade',
  jade_dest:output_dir
};

// not all tasks need to use streams
// a gulpfile is just another node program and you can use all packages available on npm
gulp.task('clean', function(cb) {
  // you can use multiple globbing patterns as you would with `gulp.src`
  del(['build'], cb);
});

gulp.task('jade',function(){
    var opts = {"pretty":true};
    return gulp.src(paths.jade)
        .pipe(plumber())
        .pipe(jade(opts))
        .pipe(gulp.dest(paths.jade_dest))
});

gulp.task('scss',function(){
    gulp.src(paths.scss)
        .pipe(plumber())
        .pipe(sass())
        .pipe(gulp.dest(paths.css_dest))

});

gulp.task('scripts', function() {
  // minify and copy all javascript (except vendor scripts)
  // with sourcemaps all the way down
    //  ignore uglify() 　 for develop
  return gulp.src(paths.scripts)
        .pipe(plumber())
        .pipe(sourcemaps.init())
        .pipe(coffee())
        .pipe(concat('app_v2.js'))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(paths.scripts_dest));
});
gulp.task('build',['jade','scripts','bower','scss'],function(){
    console.log("login task");

});

gulp.task('bower',function(){
    var jsFilter = gulpFilter('**/*.js');
    var cssFilter = gulpFilter('**/*.css');
    var fontFilter =gulpFilter(['*.otf','*.eot','*.woff','*.svg','*.ttf']);
    var files = mainBowerFiles();
    gulp.src(files)
        .pipe(jsFilter)
        .pipe(gulp.dest(paths.scripts_dest+'/vendor'));
    gulp.src(files)
        .pipe(cssFilter)
        .pipe(gulp.dest(paths.css_dest));

    gulp.src(files)
        .pipe(fontFilter)
        .pipe(gulp.dest(paths.font_dest));

});

// Copy all static images
gulp.task('images', ['clean'], function() {
  return gulp.src(paths.images)
    // Pass in options to the task
    .pipe(imagemin({optimizationLevel: 5}))
    .pipe(gulp.dest('build/img'));
});

// Rerun the task when a file changes
gulp.task('watch', function() {
  gulp.watch(paths.jade,['jade']);
  gulp.watch(paths.scripts, ['scripts']);
  gulp.watch(paths.scss,['scss'])
  //gulp.watch(paths.images, ['images']);
});

// The default task (called when you run `gulp` from cli)
gulp.task('default', ['watch', 'build']);
