# Script used to remove PII and opinions from data
# Liam Fruzyna 2023-03-21

import sys, os, json

# check for path argument
if len(sys.argv) < 2:
    print('Requires path as argument')
    exit(1)

dir = sys.argv[1]

# go over every json file in given directory
for filename in os.listdir(dir):
    path = os.path.join(dir, filename)
    if os.path.isfile(path) and filename.endswith('.json'):
        obj = None

        # read json
        with open(path, 'r') as f:
            obj = json.load(f)

            # replace values
            if not isinstance(obj, list) and not isinstance(obj, str):
                # remove school and grad year from student IDs
                if 'meta_scouter_id' in obj.keys():
                    obj['meta_scouter_id'] -= obj['meta_scouter_id'] // 1000 * 1000
                if 'meta_note_scouter_id' in obj.keys():
                    obj['meta_note_scouter_id'] -= obj['meta_note_scouter_id'] // 1000 * 1000
                # remove ratings
                if 'match_tele_driver_driver_skill' in obj.keys():
                    obj['match_tele_driver_driver_skill'] = 0
                if 'pit_pit_other_build_quality' in obj.keys():
                    obj['pit_pit_other_build_quality'] = 0
                # remove notes
                if 'match_tele_post_match_notes' in obj.keys():
                    obj['match_tele_post_match_notes'] = 'Removed'
                if 'note_notes_team_notes' in obj.keys():
                    obj['note_notes_team_notes'] = 'Removed'
                if 'pit_pit_other_notes' in obj.keys():
                    obj['pit_pit_other_notes'] = 'Removed'

        # rewrite json
        with open(path, 'w') as f:
            if obj is not None:
                f.write(json.dumps(obj))
