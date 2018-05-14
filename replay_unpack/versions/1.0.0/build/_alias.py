g_aliasMap = {'DESTRUCTIBLE_ATTACK_INFO': ['FIXED_DICT', [('hitPoint', 'VECTOR3'), ('shotID', 'INT32'), ('attacker', 'ATTACKER_INFO')], True], 'QUEUE_INFO': 'PYTHON', 'PUBLIC_CHAT_CHANNEL_INFO': ['FIXED_DICT', [('id', 'OBJECT_ID'), ('channelName', 'STRING'), ('isReadOnly', 'BOOL'), ('isSecured', 'BOOL'), ('flags', 'UINT8')], False], 'STUN_INFO': 'FLOAT64', 'REMOTE_CAMERA_DATA': ['FIXED_DICT', [('time', 'FLOAT64'), ('shotPoint', 'VECTOR3'), ('zoom', 'UINT8')], False], 'FALLOUT_QUEUE_INFO': ['FIXED_DICT', [('classes', ['ARRAY', 'UINT32']), ('players', 'UINT32')], True], 'RESPAWN_COOLDOWN_ITEM': ['FIXED_DICT', [('vehTypeCompDescr', 'UINT16'), ('endOfCooldownPiT', 'FLOAT32')], False], 'BATTLE_EVENTS_SUMMARY': ['FIXED_DICT', [('damage', 'UINT32'), ('trackAssist', 'UINT32'), ('radioAssist', 'UINT32'), ('stunAssist', 'UINT32'), ('smokeAssist', 'UINT32'), ('inspireAssist', 'UINT32'), ('tankings', 'UINT32'), ('lastKillerID', 'OBJECT_ID'), ('lastDeathReasonID', 'UINT8')], False], 'GENERIC_MESSENGER_ARGS_chat2': ['FIXED_DICT', [('int32Arg1', 'INT32'), ('int64Arg1', 'INT64'), ('floatArg1', 'FLOAT64'), ('strArg1', 'STRING'), ('strArg2', 'STRING')], False], 'DISCLOSE_EVENT': ['FIXED_DICT', [('vehicleID', 'OBJECT_ID'), ('playerName', 'BOOL'), ('vehicleType', 'BOOL')], False], 'AVATAR_AMMO_VIEWS': ['FIXED_DICT', [('vehTypeCompDescrs', ['ARRAY', 'INT32']), ('compDescrs', ['ARRAY', 'LIST_OF_COMP_DESCRS'])], False], 'PUBLIC_ARENA_INFO': ['FIXED_DICT', [('id', 'OBJECT_ID'), ('typeID', 'INT32'), ('roundLength', 'INT32'), ('roundStart', 'FLOAT32')], False], 'AVATAR_VEHICLE_ROSTER': ['FIXED_DICT', [('vehicleID', 'OBJECT_ID'), ('prebattleID', 'OBJECT_ID'), ('team', 'INT8'), ('observer', 'BOOL')], False], 'PUBLIC_VEHICLE_INFO': ['FIXED_DICT', [('name', 'STRING'), ('compDescr', 'STRING'), ('outfit', 'STRING'), ('index', 'UINT8'), ('team', 'UINT8'), ('prebattleID', 'OBJECT_ID'), ('marksOnGun', 'UINT8')], False], 'EVENT_QUEUE_INFO': ['FIXED_DICT', [('classes', ['ARRAY', 'UINT32']), ('players', 'UINT32')], True], 'PUBLIC_USERS_ROSTER_MEMBER_INFO': ['FIXED_DICT', [('id', 'DB_ID'), ('nickName', 'STRING'), ('accessFlags', 'UINT8')], False], 'OBJECT_ID': 'INT32', 'VEHICLE_SYNC_ATTRS': ['FIXED_DICT', [('circularVisionRadius', 'UINT16')], False], 'BOUNDS2': ['ARRAY', 'VECTOR2', 2], 'CLIENT_STATISTICS': ['FIXED_DICT', [('fpsMin', 'INT16'), ('fpsMax', 'INT16'), ('fpsAvg', 'INT16'), ('fps_0_5', 'INT16'), ('fps_6_10', 'INT16'), ('fps_11_15', 'INT16'), ('fps_16_20', 'INT16'), ('fps_21_25', 'INT16'), ('fps_26_30', 'INT16'), ('fps_31_35', 'INT16'), ('fps_36_40', 'INT16'), ('fps_gt_40', 'INT16'), ('fps_41_45', 'INT16'), ('fps_46_50', 'INT16'), ('fps_51_55', 'INT16'), ('fps_56_60', 'INT16'), ('fps_61_70', 'INT16'), ('fps_71_80', 'INT16'), ('fps_81_90', 'INT16'), ('fps_91_100', 'INT16'), ('fps_101_120', 'INT16'), ('fps_121_140', 'INT16'), ('fps_141_160', 'INT16'), ('fps_161_180', 'INT16'), ('fps_gt_180', 'INT16'), ('fpsDeviation', 'INT16'), ('ping', 'INT16'), ('lag', 'UINT8'), ('graphicsPreset', 'UINT8'), ('screenResWidth', 'INT16'), ('screenResHeight', 'INT16'), ('windowMode', 'UINT8'), ('drrScale', 'UINT8'), ('gameSessionDuration', 'INT16'), ('cameraPos', 'VECTOR3'), ('cameraDir', 'VECTOR3'), ('availVMem', 'INT32'), ('invalidStats', 'UINT32'), ('activeTime', 'UINT32'), ('loadingTime', 'UINT32'), ('dynamicDRR', 'UINT8'), ('soundQuality', 'UINT8'), ('graphicsSettings', 'UINT64'), ('hangarLoadingTime', 'FLOAT'), ('lastArenaUniqueID', 'UINT64'), ('lastArenaTypeID', 'UINT32'), ('lastArenaTeam', 'UINT16')], True], 'VEHICLE_SPATIAL_INFO': ['FIXED_DICT', [('vehicleID', 'OBJECT_ID'), ('team', 'UINT8'), ('position', 'VECTOR3'), ('isAlive', 'BOOL'), ('vehClass', 'STRING'), ('prebattleID', 'OBJECT_ID')], False], 'FRONT_LINE_DATA': ['FIXED_DICT', [('columnWidth', 'FLOAT'), ('frontDropPerColumn', 'FLOAT'), ('outlierFraction', 'FLOAT'), ('outlierVerticalDistance', 'FLOAT'), ('intrusionVerticalTolerance', 'FLOAT'), ('intrusionCheckExtendBounds', 'FLOAT'), ('defenderTeam', 'UINT8'), ('frontEdgeExtendColumns', 'UINT8'), ('frontLineIds', ['ARRAY', 'UINT8']), ('frontLineBounds', ['ARRAY', 'BOUNDS2']), ('frontLineMainDirVecs', ['ARRAY', 'VECTOR2'])], False], 'SHOT_ID': 'INT32', 'RANKED_BATTLES_QUEUE_INFO': ['FIXED_DICT', [('classes', ['ARRAY', 'UINT32']), ('players', 'UINT32')], True], 'DB_ID': 'INT64', 'PREBATTLE_RESULTS': ['FIXED_DICT', [('winner', 'UINT8'), ('finishReason', 'UINT8'), ('kickReason', 'UINT8'), ('extendedResults', 'PYTHON')], True], 'RESPAWN_LIMITED_VEHICLES': ['FIXED_DICT', [('group', 'UINT8'), ('vehTypeCompDescrs', ['ARRAY', 'UINT16'])], False], 'SpaceToD': ['FIXED_DICT', [('initialTimeOfDay', 'FLOAT'), ('gameSecondsPerSecond', 'FLOAT')], False], 'BATTLE_EVENT': ['FIXED_DICT', [('eventType', 'UINT8'), ('targetID', 'OBJECT_ID'), ('details', 'UINT64'), ('count', 'UINT16')], False], 'SERVER_STATISTICS': ['FIXED_DICT', [('clusterCCU', 'UINT32'), ('regionCCU', 'UINT32')], False], 'ATTACK_RESULTS': ['FIXED_DICT', [('targetID', 'OBJECT_ID'), ('targetVehicleIndex', 'UINT8'), ('targetTeam', 'UINT8'), ('targetTypeCompDescr', 'UINT16'), ('targetIsTeamKiller', 'BOOL'), ('targetIsOnTheIgnoredBase', 'BOOL'), ('targetIsOnTheCapturableBase', 'BOOL'), ('targetIsNotSpotted', 'BOOL'), ('targetMaxHealth', 'UINT16'), ('targetHealthBeforeDamage', 'INT16'), ('enemiesNearTarget', 'UINT8'), ('isRecoil', 'BOOL'), ('reason', 'UINT8'), ('shellCompDescr', 'INT32'), ('hitIndirection', 'UINT8'), ('shotID', 'SHOT_ID'), ('numVehiclesAffected', 'INT16'), ('hitFlags', 'INT32'), ('crits', 'INT32'), ('stunDuration', 'FLOAT32'), ('allCrits', 'INT32'), ('anyDeviceWasDamaged', 'BOOL'), ('damage', 'INT32'), ('repairCost', 'UINT32'), ('critBonusFactor', 'FLOAT32'), ('droppedCapturePoints', 'FLOAT32'), ('trackAssistants', ['ARRAY', 'OBJECT_ID']), ('stunAssistants', ['ARRAY', 'OBJECT_ID']), ('smokeAssistants', ['ARRAY', 'OBJECT_ID']), ('distance', 'FLOAT32'), ('targetInitialSpeed', 'FLOAT32'), ('attackerInitialSpeed', 'FLOAT32'), ('attackerHullDamage', 'UINT16'), ('attackerKilledHimself', 'BOOL'), ('attackerHealthBeforeDamage', 'INT16'), ('circularVisionRadius', 'FLOAT32'), ('attackerWasInvisible', 'BOOL'), ('equipmentID', 'UINT16'), ('targetWithFlag', 'BOOL'), ('isIronShieldDamage', 'BOOL'), ('attackerType', 'UINT8')], False], 'VEHICLE_DETECTOR_INFO': ['FIXED_DICT', [('detectorID', 'UINT16'), ('point', 'VECTOR3'), ('radius', 'FLOAT32'), ('aliveOnly', 'BOOL')], False], 'RESPAWN_AVAILABLE_VEHICLE': ['FIXED_DICT', [('compDescr', 'STRING'), ('crewCompactDescrs', ['ARRAY', 'STRING']), ('marksOnGun', 'UINT8'), ('vehAmmo', ['ARRAY', 'INT32']), ('settings', 'UINT16')], False], 'ATTACKER_INFO': ['FIXED_DICT', [('baseMB', 'MAILBOX'), ('receiveAttackResultsMB', 'MAILBOX'), ('team', 'UINT8'), ('position', 'VECTOR3'), ('circularVisionRadius', 'FLOAT32'), ('health', 'INT16'), ('noOwner', 'BOOL'), ('attackerInitialSpeed', 'FLOAT32'), ('attackerWasInvisible', 'BOOL'), ('attackerTypeCompactDescr', 'UINT16'), ('attackerVehicleIndex', 'UINT8'), ('attackerGunBurstCount', 'UINT8'), ('equipmentID', 'UINT16'), ('attackerType', 'UINT8')], False], 'RESPAWN_INFO': ['FIXED_DICT', [('compDescr', 'STRING'), ('respawnType', 'UINT8'), ('autoRespawnPiT', 'FLOAT32'), ('manualRespawnPiT', 'FLOAT32')], False], 'SMOKE_INFO': ['FIXED_DICT', [('smokeID', 'UINT16'), ('equipmentID', 'UINT16'), ('endTime', 'FLOAT64')], False], 'RANDOMS_QUEUE_INFO': ['FIXED_DICT', [('classes', ['ARRAY', 'UINT32'])], True], 'ARENA_VEH_INFO': ['FIXED_DICT', [('vehInvID', 'INT32'), ('vehCompDescr', 'STRING'), ('vehOutfit', 'STRING'), ('vehAmmo', ['ARRAY', 'INT32']), ('vehCrew', ['ARRAY', 'STRING']), ('vehCrewInvIDs', ['ARRAY', 'INT32']), ('marksOnGun', 'UINT8'), ('isRent', 'BOOL'), ('activeRent', 'UINT8'), ('settings', 'UINT16')], False], 'CLIENT_SYSTEM': ['FIXED_DICT', [('isLaptop', 'UINT8'), ('cpuVendor', 'UINT8'), ('cpuCores', 'UINT8'), ('cpuFreq', 'INT16'), ('gpuVendor', 'UINT8'), ('gpuMemory', 'INT16'), ('mainMemory', 'INT32'), ('os', 'INT32'), ('graphicsEngine', 'UINT8'), ('cpuScore', 'INT32'), ('gpuScore', 'INT16'), ('osBit', 'UINT8'), ('hasMods', 'UINT8'), ('cpuFamily', 'UINT32'), ('gpuFamily', 'UINT32'), ('crashed', 'UINT64'), ('contentType', 'UINT8'), ('gpuDriverVersion', 'INT64'), ('graphicsAPIID', 'UINT32'), ('multiGPU', 'UINT8'), ('cpuName', 'STRING'), ('hangarFirstLoadingTime', 'FLOAT')], True], 'CHAT_ACTION_DATA': ['FIXED_DICT', [('requestID', 'INT64'), ('action', 'UINT8'), ('actionResponse', 'UINT8'), ('time', 'FLOAT64'), ('sentTime', 'FLOAT64'), ('channel', 'OBJECT_ID'), ('originator', 'DB_ID'), ('originatorNickName', 'STRING'), ('group', 'UINT8'), ('data', 'PYTHON'), ('flags', 'UINT8')], False], 'PREBATTLE_INVITE': ['FIXED_DICT', [('createTime', 'UINT32'), ('type', 'UINT16'), ('comment', 'STRING'), ('creator', 'STRING'), ('creatorBadges', ['ARRAY', 'UINT32']), ('creatorDBID', 'DB_ID'), ('creatorClanAbbrev', 'STRING'), ('extraData', 'PYTHON')], False], 'LIST_OF_COMP_DESCRS': ['ARRAY', 'INT32'], 'EXTRA_ID': 'UINT8', 'INSPIRING_EFFECT': ['FIXED_DICT', [('radius', 'FLOAT32'), ('startTime', 'FLOAT64'), ('endTime', 'FLOAT64'), ('inactivationDelay', 'FLOAT32')], True], 'RESPAWN_INFO_VEHICLE': ['FIXED_DICT', [('compDescr', 'STRING'), ('crewCompactDescrs', ['ARRAY', 'STRING']), ('marksOnGun', 'UINT8'), ('index', 'UINT16'), ('position', 'VECTOR3'), ('yaw', 'FLOAT32'), ('prevGroup', 'UINT8'), ('group', 'UINT8'), ('policyID', 'UINT8'), ('onRespawnSettings', 'PYTHON'), ('ammo', ['ARRAY', 'INT32']), ('outfit', 'STRING')], False], 'BOOL': 'UINT8', 'EPIC_QUEUE_INFO': ['FIXED_DICT', [('classes', ['ARRAY', 'UINT32']), ('players', 'UINT32')], True], 'INSPIRED': ['FIXED_DICT', [('startTime', 'FLOAT64'), ('endTime', 'FLOAT64'), ('inactivationStartTime', 'FLOAT64'), ('inactivationEndTime', 'FLOAT64')], True], 'ARENA_ADDPLAYER_INFO': ['FIXED_DICT', [('name', 'STRING'), ('attrs', 'UINT64'), ('databaseID', 'DB_ID'), ('centerID', 'INT32'), ('clanAbbrev', 'STRING'), ('clanDBID', 'DB_ID'), ('prebattle', 'MAILBOX'), ('isPrebattleCreator', 'BOOL'), ('forbidInBattleInvitations', 'BOOL'), ('team', 'UINT8'), ('tkillRating', 'FLOAT'), ('cybersportRating', ['ARRAY', 'FLOAT']), ('globalRating', 'FLOAT'), ('igrType', 'INT8'), ('potapovQuestIDs', ['ARRAY', 'UINT16']), ('vehiclesInfo', ['ARRAY', 'ARENA_VEH_INFO']), ('avatarAmmo', ['ARRAY', 'INT32']), ('needCheckPenalties', 'BOOL'), ('fairplayState', 'PYTHON'), ('battlesNum', 'UINT32'), ('ranked', 'PYTHON'), ('group', 'UINT8'), ('historicallyAccurate', 'BOOL')], False]}