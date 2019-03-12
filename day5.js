let polymer="" // Input polymer goes here...


class PolymerProcessor {
  constructor(inputPolymer) {
    this.input = inputPolymer;
    this.processingStack = [];
    this.outputLength_ = undefined;
  }

  processPolymer() {
    console.log("processing polymer ...");
    for (let character of this.input) {
      this.pushToStack(character);
    }
    this.outputLength_ = this.processingStack.length;
  }

  pushToStack(incomingCharacter) {
    let topStackCharacter = this.processingStack.length
      ? this.processingStack[this.processingStack.length - 1]
      : null;
    let breakDownCondition = topStackCharacter && topStackCharacter !== incomingCharacter && topStackCharacter.toLowerCase() === incomingCharacter.toLowerCase();
    if (breakDownCondition) {
      this.processingStack.pop();
    } else {
      this.processingStack.push(incomingCharacter);
    }
  }

  get outputLength() {
    if (this.outputLength_ === undefined) {
      this.processPolymer();
    }
    return this.outputLength_;
  }

  get outputPolymer() {
    if (this.processingStack.length === 0) {
      this.processPolymer();
    }
    return this.processingStack.join("");
  }
}

function breakDown() {
  pp = new PolymerProcessor(polymer);
  pp.processPolymer();
  console.log(pp.outputLength);
  console.log(pp.outputPolymer);
}
