/* ---------------------------------------------------------------------------
 * Filter Courses.
 * --------------------------------------------------------------------------- */

// Course container.
let $grid_courses = $('#container-courses');

let $semester_filter = $('.courses-filter');

let semesterValue = $semester_filter.children("option:selected").val();

// Initialise Isotope.
$grid_courses.isotope({
  layoutMode: 'vertical',
  vertical: {
    horizontalAlignment: 0.5,
  },
  hiddenStyle: {
    position: 'relative',
    display: 'none'
  },
  visibleStyle: {
    position: 'relative',
    display: 'flex'
  }
});

// hash of functions that match data-filter values
const filterFns = {
  semester: function () {
    // use $(this) to get item element
    let semesterClass = "semester-" + semesterValue;
    return $(this).hasClass(semesterClass);
  },
};

// filter items on button click
$semester_filter.on('change', function () {
  semesterValue = $(this).children("option:selected").val();
  let filterValue = $(this).attr('data-filter');
  // use filter function if value matches
  filterValue = filterFns[ filterValue ] || filterValue;
  $grid_courses.isotope({ filter: filterValue });
  console.log(semesterValue);
});

// Filter courses according to hash in URL.
function filter_courses() {
  let urlHash = window.location.hash.replace('#', '');

  // Check if semester hash is valid
  if (urlHash !== '' && urlHash.match(/\d{4}[SW]/)) {
    semesterValue = urlHash;
  }

  let filterValue = filterFns['semester'];
  $grid_courses.isotope({ filter: filterValue });

  // Set selected option.
  $semester_filter.val(semesterValue);
}

$(window).on('load', function () {
  // Enable course filter for course index page.
  if ($('.courses-widget')) {
    console.log(semesterValue);
    filter_courses();
    // Useful for changing hash manually (e.g. in development):
    // window.addEventListener('hashchange', filter_courses, false);
  }
});
