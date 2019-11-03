const express = require('express');
const members = require('../../Members');
const uuid  = require('uuid');

const router = express.Router();

// GET ALL MEMBERS
router.get('/', (req, res) => res.json(members));

// GET SINGLE MEMBER
router.get('/:id', (req, res) => {
    const memberId = req.params.id;
    const memberWithParamId = members.find(member => member.id === memberId);

    memberWithParamId
        ? res.json(memberWithParamId)
        : res.status(400).json({ msg: `No member with the id of ${req.params.id}` })

});

// CREATE MEMBER
router.post('/', (req, res) => {
    const newMember = {
        id: uuid.v4(),
        name: req.body.name,
        email: req.body.email,
        status: 'active'
    };

    if(!newMember.name || !newMember.email) {
        return res.status(400).json({ msg: 'Please include a name and email' });
    }

    members.push(newMember);
    res.redirect('/');
});

// UPDATE MEMBER
router.put('/:id', (req, res) => {
    const memberId = req.params.id;
    const found = members.some(member => member.id === memberId);

    if (found) {
        const updMember = req.body;
        members.forEach(member => {
            if (member.id === memberId) {
                member.name = updMember.name ? updMember.name : member.name;
                member.email = updMember.email ? updMember.email : member.email;

                res.json({ msg: 'Member updated', member })
            }
        });
    } else {
        res.status(400).json({ msg: `No member with the id of ${req.params.id}` })
    }

});

// DELETE MEMBER
router.delete('/:id', (req, res) => {
    const memberId = req.params.id;
    const found = members.some(member => member.id === memberId);

    if (found) {
        res.json({ msg: 'member deleted', members: members.filter(member => member.id !== memberId)})
    } else {
        res.status(400).json({ msg: `No member with the id of ${req.params.id}` })
    }

});


module.exports = router;