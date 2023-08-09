var title = document.getElementById('title');

var typewriter = new Typewriter(title, {
    loop: true
});

typewriter.typeString('Free-thinking Fusionpreneur')
    .pauseFor(2500)
    .deleteAll()
    .typeString('Concept Consultant  ')
    .pauseFor(2500)
    .deleteAll()
    .typeString('<strong>Performing Presenter</strong>')
    .pauseFor(2500)
    .start();