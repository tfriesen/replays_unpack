#!/usr/bin/python
# coding=utf-8
from build.entities import Avatar

__author__ = "Aleksandr Shyshatsky"


class Avatar(Avatar):
    def __init__(self):
        Avatar.__init__(self)
        self.methodsMap = {
            65: 'setClientReady',
            66: 'leaveArena',
            68: 'confirmBattleResultsReceiving',
            69: 'makeDenunciation',
            70: 'banUnbanUser',
            71: 'requestToken',
            73: 'sendAccountStats',
            74: 'setClientCtx',
            78: 'vehicle_moveWith',
            79: 'vehicle_shoot',
            80: 'vehicle_trackWorldPointWithGun',
            82: 'vehicle_stopTrackingWithGun',
            83: 'vehicle_changeSetting',
            84: 'vehicle_teleport',
            85: 'vehicle_replenishAmmo',
            92: 'setVehicleDevelopmentFeature',
            93: 'setDevelopmentFeature',
            94: 'addBotToArena',
            95: 'receiveFakeShot',
            96: 'logStreamCorruption',
            4: 'autoAim',
            5: 'moveTo',
            6: 'bindToVehicle',
            7: 'monitorVehicleDamagedDevices',
            23: 'activateEquipment',
            24: 'setEquipmentApplicationPoint',
            26: 'switchViewPointOrBindToVehicle',
            28: 'update',
            29: 'onKickedFromServer',
            30: 'onIGRTypeChanged',
            31: 'onAutoAimVehicleLost',
            32: 'receiveAccountStats',
            33: 'updateVehicleHealth',
            34: 'updateVehicleGunReloadTime',
            35: 'updateVehicleClipReloadTime',
            36: 'updateVehicleAmmo',
            37: 'onSwitchViewpoint',
            38: 'onBootcampEvent',
            40: 'updateVehicleMiscStatus',
            41: 'updateVehicleSetting',
            42: 'updateTargetingInfo',
            43: 'updateGunMarker',
            44: 'updateOwnVehiclePosition',
            45: 'showOwnVehicleHitDirection',
            46: 'showVehicleDamageInfo',
            47: 'showOtherVehicleDamagedDevices',
            48: 'showShotResults',
            49: 'updatePlaneTrajectory',
            50: 'showHittingArea',
            51: 'showCarpetBombing',
            52: 'showDevelopmentInfo',
            53: 'showTracer',
            54: 'stopTracer',
            55: 'explodeProjectile',
            56: 'onRoundFinished',
            57: 'onKickedFromArena',
            58: 'onBattleEvents',
            59: 'battleEventsSummary',
            60: 'updateArena',
            61: 'updatePositions',
            62: 'receivePhysicsDebugInfo',
            63: 'updateCarriedFlagPositions',
            64: 'receiveNotification',
            65: 'onRepairPointAction',
            66: 'updateAvatarPrivateStats',
            67: 'updateResourceAmount',
            68: 'updateGasAttackState',
            69: 'syncVehicleAttrs',
            70: 'onFrictionWithVehicle',
            71: 'onCollisionWithVehicle',
            72: 'onSmoke',
            73: 'onCombatEquipmentShotLaunched',
        }
