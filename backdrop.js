const _createHighlight = ({ xMin, xMax, yMin, yMax, color }, hDistance, vDistance, vTopSpace) => {
  const backDrop = document.querySelector("#backdrop");

  for (let xIndex = xMin; xIndex <= xMax; xIndex++) {
    const rectLeftSpace = 50;
    const x = rectLeftSpace + (xIndex - 0.5) * hDistance;

    for (let yIndex = yMin; yIndex <= yMax; yIndex++) {
      const rectTopSpace = vTopSpace + 51;
      const y = rectTopSpace + yIndex * vDistance;
      let rectangle = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "rect"
      );
      rectangle.setAttribute("x", `${x}`);
      rectangle.setAttribute("y", `${y}`);
      rectangle.setAttribute("width", `${hDistance - 1}`);
      rectangle.setAttribute("height", `${vDistance - 1}`);
      rectangle.setAttribute("fill", color);
      backDrop.appendChild(rectangle);
    }
  }
};

const _createGridLabels = (maxX, maxY, hDistance, vDistance, vTopSpace) => {
  const backDrop = document.querySelector("#backdrop");

  for (let xIndex = 0; xIndex <= maxX; xIndex++) {
    const rectLeftSpace = 50;
    const x = rectLeftSpace + (xIndex - 0.5) * hDistance;
    const y = vTopSpace + 52 + vDistance * maxY;

    var text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", `${x + 22}`);
    text.setAttribute("y", `${y + 59}`);
    text.textContent = `${xIndex}`;
    text.setAttribute("font-size", "24");
    backDrop.appendChild(text);
  }

  for (let yIndex = 0; yIndex <= maxY; yIndex++) {
    const rectLeftSpace = 20;
    const x = rectLeftSpace;
    const rectTopSpace = vTopSpace + 51;
    const y = rectTopSpace + yIndex * vDistance;

    var text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", `${x - 20}`);
    text.setAttribute("y", `${y + 25}`);
    text.textContent = `${yIndex}`;
    text.setAttribute("font-size", "24");

    backDrop.appendChild(text);
  }
};

const recreateBackdrop = (maxX, maxY, hDistance, vDistance, vTopSpace, highlights) => {
  const backDrop = document.querySelector("#backdrop");

  while (backDrop.firstChild) {
    backDrop.removeChild(backDrop.firstChild);
  }

  _createHighlight({
    xMin: 0,
    xMax: maxX,
    yMin: 0,
    yMax: maxY,
    color: "lightgray",
  }, hDistance, vDistance, vTopSpace);

  highlights.forEach((highlight) => {
    _createHighlight(highlight, hDistance, vDistance, vTopSpace);
  });
  _createGridLabels(maxX, maxY, hDistance, vDistance, vTopSpace);
};
