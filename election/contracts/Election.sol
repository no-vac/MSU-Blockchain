pragma solidity 0.4.24;

contract Election{
    struct Candidate{
        uint id;
        string name;
        uint voteCount;
    }

    // read/write candidates
    mapping(uint => Candidate) public candidates;

    // store candidate count
    uint public candidatesCount;


    function addCandidate(string _name) private{
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
    }

    constructor () public {
        addCandidate("Candidate 1");
        addCandidate("Candidate 2");
    }
    
}

