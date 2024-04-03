const {
  time,
  loadFixture,
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");
const { expect } = require("chai");

describe("Counter", function () {
  // We define a fixture to reuse the same setup in every test.
  // We use loadFixture to run this setup once, snapshot that state,
  // and reset Hardhat Network to that snapshot in every test.
  async function deployCounterkFixture() {
    // Contracts are deployed using the first signer/account by default
    const [owner, otherAccount] = await ethers.getSigners();

    const Counter = await ethers.getContractFactory("Counter");
    const counter = await Counter.deploy();

    return { counter, owner, otherAccount };
  }

  describe("Deployment", function () {
    it("Should set the count value to 0", async function () {
      const { counter } = await loadFixture(deployCounterkFixture);

      expect(await counter.count()).to.equal(0);
    });
  });

  describe("pressBtn", function () {
    describe("Events", function () {
      it("Should increase count", async function () {
        const { counter  } = await loadFixture(
          deployCounterkFixture
        );

        await counter.pressBtn()
        await counter.pressBtn()

        expect(await counter.count()).to.eq(2)
      });
    });

  });
});
